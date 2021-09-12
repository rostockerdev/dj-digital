from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from courses.models import Course
from instructors.models import Instructor


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changfreq = "daily"

    def items(self):
        return ["pages:faqs"]

    def location(self, item):
        return reverse(item)


class CourseSitemap(Sitemap):
    changfreq = "daily"
    priority = 0.9

    def items(self):
        return Course.objects.all().order_by("-start_date")

    def location(self, item):
        return reverse("courses:course-detail", kwargs={"course_slug": item.slug})


class InstructorSitemap(Sitemap):
    chagefreq = "daily"
    priority = 0.9

    def items(self):
        return Instructor.objects.all().order_by("-dofb")

    def location(self, item):
        return reverse(
            "instructors:instructor-detail", kwargs={"instructor_name": item.username}
        )
