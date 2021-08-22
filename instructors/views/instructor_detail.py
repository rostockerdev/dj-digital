from django.shortcuts import render
from django.views.generic import DetailView

from instructors.forms import RatingForm
from instructors.models import Instructor


class InstructorDetailView(DetailView):
    def get(self, *args, **kwargs):
        username = kwargs["instructor_name"]
        instructor = Instructor.objects.get(username=username)
        form = RatingForm()
        context = {"instructor": instructor, "form": form}
        return render(self.request, "instructors/instructor_detail.html", context)
