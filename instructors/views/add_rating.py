import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from instructors.forms import RatingForm
from instructors.models import Instructor, Rating


@login_required
def AddRatingView(request, instructor_name):
    print(instructor_name)
    instructor = get_object_or_404(Instructor, username=instructor_name)
    form = RatingForm(request.POST)
    rating_qr = Rating.objects.filter(user=request.user, instructor=instructor)
    if rating_qr.exists():
        messages.warning(request, "You already rated the instructor")
        return redirect("instructors:instructor-detail", instructor_name)
    else:
        if form.is_valid():
            userrating = form.cleaned_data["rating"]
            review = form.cleaned_data["review"]
            rating = Rating()
            rating.instructor = instructor
            rating.pub_date = datetime.datetime.now()
            rating.user = request.user
            rating.review = review
            rating.rating = userrating
            rating.save()
            messages.success(request, "Successfully reviewed")
            return redirect("instructors:instructor-detail", instructor_name)
        return render(
            request,
            "instructors/instructor_detail.html",
            {"form": form, "instructor": instructor},
        )
