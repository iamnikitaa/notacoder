# Generated by Django 5.1.5 on 2025-06-28 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeChallenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, help_text='URL-friendly version of the title, auto-generated.', max_length=220, unique=True)),
                ('description', models.TextField(blank=True, help_text='Instructions and context for the user.')),
                ('code_template', models.TextField()),
                ('correct_answers_list', models.JSONField(default=list, help_text='A JSON list of strings representing the exact correct answers for the blanks, IN ORDER.')),
                ('difficulty', models.PositiveSmallIntegerField(default=1, help_text='Difficulty level (e.g., 1=easy, 5=hard)')),
                ('points_reward', models.PositiveIntegerField(default=10, help_text='Points awarded for successful completion.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('magic_word', models.CharField(max_length=100)),
                ('current_challenge', models.IntegerField(default=1)),
                ('completed_challenges', models.ManyToManyField(blank=True, related_name='solved_by_users', to='core.codechallenge')),
            ],
        ),
        migrations.AddField(
            model_name='codechallenge',
            name='language',
            field=models.ForeignKey(help_text='The programming language of the code snippet.', on_delete=django.db.models.deletion.PROTECT, related_name='challenges', to='core.programminglanguage'),
        ),
        migrations.AddField(
            model_name='codechallenge',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Categorize the challenge with relevant tags.', related_name='challenges', to='core.tag'),
        ),
    ]
