from django.views.generic import ListView

from instructors.models import Instructor


class InstructorListView(ListView):
    model = Instructor
    context_object_name = "instructors"
    template_name = "instructors/instructor_list.html"
