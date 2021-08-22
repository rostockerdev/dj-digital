import datetime
import logging

from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from courses.forms import CommentForm
from courses.models import Comment, Course, Lesson


def set_expiration_time(session, var_name, expire_at):
    print(expire_at)
    session[var_name] = {"expiredat": expire_at.timestamp()}


def get_expirable_var(session, var_name, default=None):
    var = default
    if var_name in session:
        my_variable_dict = session.get(var_name, {})
        print(my_variable_dict.get("expiredat", 0))
        if my_variable_dict.get("expiredat", 0) > datetime.datetime.now().timestamp():
            return my_variable_dict.get("value")
    else:
        return None
    return var


def add_comment_view(request, course_slug, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    # course = get_object_or_404(Course, slug=course_slug)
    form = CommentForm(request.POST)
    if "expire_at" in request.session:
        expire_at = request.session["expire_at"]
        if expire_at > datetime.datetime.now().timestamp():
            messages.warning(
                request,
                "Sorry, You can not comment today. You have to wait 24 hours to comment again.",
            )
            return redirect("courses:lesson-detail", course_slug, lesson_slug)
        else:
            print("Not allowed Session Time")
            del request.session["expire_at"]
            request.session.modified = True

    else:
        print("No Session Time")

    if form.is_valid():
        try:
            msg = form.cleaned_data["msg"]
            comment = Comment()
            comment.lesson = lesson
            comment.comment_at = datetime.datetime.now()
            comment.author = request.user
            comment.msg = msg
            comment.save()
            expire_at = datetime.datetime.combine(
                datetime.date.today(), datetime.datetime.max.time()
            )
            request.session["expire_at"] = expire_at.timestamp()
            request.session["comment_id"] = comment.id
            messages.success(
                request, "You commented successfully. After approve, you will see it."
            )
            return redirect("courses:lesson-detail", course_slug, lesson_slug)
        except IntegrityError:
            messages.warning(
                request, "There was something wrong while to store your comment"
            )
            logging.getLogger("error_logger").error(
                "There was something wrong while to store the comment"
            )
    else:
        form = CommentForm()
        # context = {
        #     "form": form,
        #     "lesson": lesson,
        #     "course": course,
        #     "course_slug": course_slug,
        #     "lesson_slug": lesson_slug,
        # }
        return redirect("courses:lesson-detail", course_slug, lesson_slug)
