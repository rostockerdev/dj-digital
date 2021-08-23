from django.contrib import admin

from quizes.models import Question, Quiz, QuizParticipation


class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    list_display = ["title", "description", "lesson"]


class QuizParticipationAdmin(admin.ModelAdmin):
    model = QuizParticipation
    list_display = [
        "quiz",
        "participate_date",
        "participate_next",
        "participator",
        "quiz_score",
    ]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["ques", "option1", "option2", "option3", "option4", "answer"]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizParticipation, QuizParticipationAdmin)
admin.site.register(Question, QuestionAdmin)
