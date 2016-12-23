from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('level', 'question_text')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)