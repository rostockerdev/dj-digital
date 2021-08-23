from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from courses.models import Course, Lesson
from quizes.decorators import restrict_quiz
from quizes.models import Question, Quiz


@login_required
@restrict_quiz("Enterprise")
def quiz_view(request, course_slug, lesson_slug):
    # course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)
    quiz = Quiz.objects.get(lesson__slug=lesson.slug)
    questions = Question.objects.filter(quiz__title=quiz.title).all()
    context = {
        "questions": questions,
        "course_slug": course_slug,
        "lesson_slug": lesson_slug,
    }
    return render(request, "quizes/quiz.html", context)
