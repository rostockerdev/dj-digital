from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from accounts.models import Profile
from courses.decorators import restrict_course
from courses.forms import CommentForm
from courses.models import Course, Lesson
from memberships.models import Membership


@login_required
@restrict_course(membership_type=["Professional", "Enterprise"])
def lesson_detail_view(request, course_slug, lesson_slug):
    if request.method == "GET":
        form = CommentForm()
        course = get_object_or_404(Course, slug=course_slug)
        lesson_qr = Lesson.objects.filter(slug=lesson_slug, course__slug=course_slug)
        if lesson_qr.exists():
            lesson = get_object_or_404(Lesson, slug=lesson_slug)
            profile = get_object_or_404(Profile, user=request.user)
            profile_membership_type = profile.membership.membership_type
            selected_allowed_membership = course.allowed_membership.all()
            context = {
                "lesson": None,
                "form": form,
                "course": course,
                "course_slug": course_slug,
                "lesson_slug": lesson_slug,
            }
            if selected_allowed_membership.filter(
                membership_type=profile_membership_type
            ).exists():
                context = {
                    "lesson": lesson,
                    "form": form,
                    "course": course,
                    "course_slug": course_slug,
                    "lesson_slug": lesson_slug,
                    "title": lesson.title,
                }
                print(lesson)
                print(form)
                return render(request, "courses/lesson_detail.html", context)
            else:
                messages.warning(
                    request,
                    "You are not allowed to view more. You have to change the membership.",
                )
                return redirect("courses:course-list")
        else:
            return redirect("courses:course-list")
