from django.contrib import admin

from .models import Answer, Choice, Question, Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_start',
        'date_end',
        'description'
    )


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
    )


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'text',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'choice',
        'created',
    )
    list_filter = ('id',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
