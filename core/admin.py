from django.contrib import admin
from .models import CodeChallenge, ProgrammingLanguage, Tag
from .models import GuestUser

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Auto-fills slug from name

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CodeChallenge)
class CodeChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'difficulty', 'points_reward', 'created_at')
    list_filter = ('language', 'difficulty', 'tags', 'created_at')
    search_fields = ('title', 'description', 'code_template')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'language', 'description')
        }),
        ('Challenge Content', {
            'fields': ('code_template', 'correct_answers_list')
        }),
        ('Metadata', {
            'fields': ('difficulty', 'points_reward', 'tags')
        }),
    )