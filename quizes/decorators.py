from functools import wraps

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse

from accounts.models import Profile
from courses.models import Course, Lesson
from quizes.models import Quiz, QuizParticipation


def restrict_quiz(membership_type):
    def _method_wrapper(view_func):
        def _arguments_wrapper(request, *args, **kwargs):
            profile = get_object_or_404(Profile, user=request.user)
            profile_membership_type = profile.membership.membership_type
            if profile_membership_type in membership_type:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse("courses:courselist"))

        return _arguments_wrapper

    return _method_wrapper
