import uuid
from django.db import models, transaction, IntegrityError
from django.utils.text import slugify

class GuestUser(models.Model):
    name = models.CharField(max_length=100, unique=True)
    magic_word = models.CharField(max_length=100) 
    current_challenge = models.IntegerField(default=1)

    completed_challenges = models.ManyToManyField(
        'CodeChallenge',
        related_name='solved_by_users',
        blank=True
    )

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
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        unique=True,
        blank=True,
        max_length=220,
        help_text="URL-friendly version of the title, auto-generated."
    )
    description = models.TextField(blank=True, help_text="Instructions and context for the user.")
    code_template = models.TextField()
    language = models.ForeignKey(
        ProgrammingLanguage,
        on_delete=models.PROTECT,
        related_name='challenges',
        help_text="The programming language of the code snippet."
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
        pass

    def get_number_of_blanks(self) -> int:
        return len(self.correct_answers_list)

    def construct_full_code(self, submitted_answers: list[str]) -> str | None:
        if len(submitted_answers) != len(self.correct_answers_list):
            return None
        return self.code_template

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
