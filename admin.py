# Register your models here.
# filename: first_site/votings/admin.py

from django.contrib import admin

from .models import Question, Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ ('Questions',               {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

     
admin.site.register(Question, QuestionAdmin)
