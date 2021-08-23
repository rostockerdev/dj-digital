import datetime

from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone

from courses.models import Course, Lesson
from notifications.models import Notification
from quizes.models import Question, Quiz, QuizParticipation


def quiz_submit_view(request, course_slug, lesson_slug):
    if request.method == "POST":
        # course = Course.objects.get(slug=course_slug)
        lesson = Lesson.objects.get(slug=lesson_slug)
        quiz = Quiz.objects.get(lesson__slug=lesson.slug)
        quizquestionanswers = Question.objects.filter(quiz__title=quiz.title)[:10]
        quizscore = 0
        quizform = request.POST.copy()
        processedquiz = {}
        for quizquestionanswer in quizquestionanswers:
            processedquiz[f"q{quizquestionanswer.id}"] = quizform[
                f"q{quizquestionanswer.id}"
            ]
            if processedquiz[f"q{quizquestionanswer.id}"] == quizquestionanswer.answer:
                quizscore += 1
            else:
                quizscore += 0
        try:
            quizparticipation = QuizParticipation.objects.get(
                quiz__title=quiz.title, participator__username=request.user.username
            )
            if quizparticipation:
                print(quizparticipation)
                schedule_next = (
                    quizparticipation.participate_next
                    - datetime.datetime.now(tz=timezone.utc)
                )
                if schedule_next.days > 7:
                    quizparticipation.quiz = quiz
                    quizparticipation.quiz_score = quizscore
                    quizparticipation.participate_date = datetime.datetime.now(
                        tz=timezone.utc
                    )
                    quizparticipation.participate_next = datetime.datetime.now(
                        tz=timezone.utc
                    ) + datetime.timedelta(days=7)
                    quizparticipation.save()
                    messages.success(request, "Thank you for your reparticipation")
                    notification = Notification()
                    notification.title = (
                        f"Thankyou for your participation in { quiz.title }"
                    )
                    notification.message = f"You scored: {quizparticipation.quiz_score}. You can participate after {quizparticipation.participate_next}"
                    notification.user = request.user
                    notification.save()
                    return redirect("courses:lesson-detail", course_slug, lesson_slug)
                else:
                    messages.success(request, "You can not retake within 7 days")
                    return redirect("courses:lesson-detail", course_slug, lesson_slug)
        except Exception:
            quizparticipation = QuizParticipation()
            quizparticipation.quiz = quiz
            quizparticipation.quiz_score = quizscore
            quizparticipation.participate_date = datetime.datetime.now(tz=timezone.utc)
            quizparticipation.participate_next = datetime.datetime.now(
                tz=timezone.utc
            ) + datetime.timedelta(days=7)
            quizparticipation.participator = request.user
            quizparticipation.save()
            messages.success(request, "Thank you for your participation")
            notification = Notification()
            notification.title = f"Thankyou for your participation in { quiz.title }"
            notification.message = f"You scored: {quizparticipation.quiz_score}. You can participate after {quizparticipation.participate_next}"
            notification.user = request.user
            notification.save()
    return redirect("courses:lesson-detail", course_slug, lesson_slug)
