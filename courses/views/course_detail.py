from django.shortcuts import render
from django.views.generic import DetailView

from courses.forms import ReviewForm
from courses.models import Course


class CourseDetailView(DetailView):
    def get(self, *args, **kwargs):
        course_slug = kwargs["course_slug"]
        form = ReviewForm()
        course = Course.objects.get(slug=course_slug)
        is_liked = False
        if course.likes.filter(id=self.request.user.id).exists():
            is_liked = True
        context = {
            "course": course,
            "form": form,
            "is_liked": is_liked,
            "total_likes": course.get_total_like(),
            "title": course.title,
        }
        return render(self.request, "courses/course_detail.html", context)
