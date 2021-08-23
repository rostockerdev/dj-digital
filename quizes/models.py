from django.conf import settings
from django.db import models

from courses.models import Lesson


class Quiz(models.Model):
    title = models.CharField("Title", max_length=256)
    description = models.CharField("Description", max_length=256)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"


class QuizParticipation(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    participate_date = models.DateTimeField(
        verbose_name="Participation Time", auto_now=True, blank=True
    )
    participate_next = models.DateTimeField(null=True, blank=True)
    participator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="participants",
        on_delete=models.CASCADE,
        null=True,
    )
    quiz_score = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.quiz.title


class Question(models.Model):
    ques = models.CharField(verbose_name="Question", max_length=256)
    option1 = models.CharField("Option 1", max_length=64)
    option2 = models.CharField("Option 2", max_length=64)
    option3 = models.CharField("Option 3", max_length=64)
    option4 = models.CharField("Option 4", max_length=64)
    answer = models.CharField("Answer", max_length=10)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.ques

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
