import uuid
from django.db import models, transaction, IntegrityError
from django.utils.text import slugify

class GuestUser(models.Model):
    name = models.CharField(max_length=100, unique=True)
    magic_word = models.CharField(max_length=100) # This will be the "password"
    current_challenge = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class CodeChallenge(models.Model):
    PLACEHOLDER = "___"
    MIN_PLACEHOLDER_LENGTH = 3

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=220,
                            help_text="URL-friendly version of the title, auto-generated.")
    description = models.TextField(blank=True, help_text="Instructions and context for the user.")
    language = models.ForeignKey(
        ProgrammingLanguage,
        on_delete=models.PROTECT,
        related_name='challenges',
        help_text="The programming language of the code snippet."
    )
    code_template = models.TextField(
        help_text="The code snippet containing placeholders like '___' for the user to fill."
    )
    correct_answers_list = models.JSONField(
        default=list,
        help_text="A JSON list of strings representing the exact correct answers for the blanks, IN ORDER.",
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='challenges',
        help_text="Categorize the challenge with relevant tags."
    )
    difficulty = models.PositiveSmallIntegerField(default=1, help_text="Difficulty level (e.g., 1=easy, 5=hard)")
    points_reward = models.PositiveIntegerField(default=10, help_text="Points awarded for successful completion.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.title} ({self.language.name})"

    def get_absolute_url(self):
        from django.urls import reverse
        try:
            return reverse('challenge_detail', kwargs={
                'lang_slug': self.language.slug,
                'challenge_slug': self.slug
            })
        except Exception:
            return '#'

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.PLACEHOLDER not in self.code_template:
            raise ValidationError({
                'code_template': f'Template must contain at least one placeholder ({self.PLACEHOLDER})'
            })

        similar_placeholders = {'__', '____'}
        for wrong in similar_placeholders:
            if wrong in self.code_template:
                raise ValidationError({
                    'code_template': f'Invalid placeholder found: {wrong}. Use {self.PLACEHOLDER}'
                })

    def get_number_of_blanks(self) -> int:
        return self.code_template.count(self.PLACEHOLDER)

    def construct_full_code(self, submitted_answers: list[str]) -> str | None:
        if len(submitted_answers) != self.get_number_of_blanks():
            return None

        filled_code = self.code_template
        for answer in submitted_answers:
            filled_code = filled_code.replace(self.PLACEHOLDER, answer, 1)

        return filled_code

    def check_submission(self, submitted_answers: list[str]) -> bool:
        if len(submitted_answers) != len(self.correct_answers_list):
            return False

        return all(
            submitted.strip() == correct.strip()
            for submitted, correct in zip(submitted_answers, self.correct_answers_list)
        )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
