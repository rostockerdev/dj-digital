# from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from courses.models import Course


def course_like_toggle_view(request, course_slug):
    course = get_object_or_404(Course, slug=request.POST.get("course_slug"))
    user = request.user
    is_liked = False
    if user.is_authenticated:
        if course.likes.filter(id=user.id).exists():
            course.likes.remove(user)
            is_liked = False
        else:
            course.likes.add(user)
            is_liked = True
    context = {
        "course": course,
        "is_liked": is_liked,
        "total_likes": course.get_total_like(),
    }
    if request.is_ajax():
        html = render_to_string("courses/course_like.html", context, request=request)
        return JsonResponse({"form": html})
