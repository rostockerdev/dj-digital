from django.core.management.base import BaseCommand

from courses.models import Course
from instructors.models import Instructor
from memberships.models import Membership


class Command(BaseCommand):
    help = "Add instructors to the Database"

    def handle(self, *args, **options):

        for _ in range(3):
            if _ == 0:
                free_membership = Membership.objects.filter(slug="Free")
                first_instructor = Instructor.objects.filter(username="instructorone")
                course_one = Course.objects.create(
                    title="Course One",
                    description="Dolor aliquip fugiat exercitation veniam in ipsum et nulla.",
                    extra_info="Adipisicing labore culpa commodo eu pariatur enim fugiat eu amet qui. Esse ullamco culpa consequat nisi pariatur eiusmod elit nulla. Duis cillum cillum veniam ullamco deserunt ipsum. Proident sunt reprehenderit cupidatat nisi qui aliqua ea labore enim.",
                )
                course_one.allowed_membership.set(free_membership)
                course_one.instructors.set(first_instructor)
                course_one.save()

            elif _ == 1:
                profissional_membership = Membership.objects.filter(slug="Professional")
                second_instructor = Instructor.objects.filter(username="instructortwo")
                course_two = Course.objects.create(
                    title="Course Two",
                    description="Dolor aliquip fugiat exercitation veniam in ipsum et nulla.",
                    extra_info="Adipisicing labore culpa commodo eu pariatur enim fugiat eu amet qui. Esse ullamco culpa consequat nisi pariatur eiusmod elit nulla. Duis cillum cillum veniam ullamco deserunt ipsum. Proident sunt reprehenderit cupidatat nisi qui aliqua ea labore enim.",
                )
                course_two.allowed_membership.set(profissional_membership)
                course_two.instructors.set(second_instructor)
                course_two.save()
            elif _ == 2:
                enterprise_membership = Membership.objects.filter(slug="Enterprise")
                third_instructor = Instructor.objects.filter(username="instructorthree")
                course_three = Course.objects.create(
                    title="Course Three",
                    description="Dolor aliquip fugiat exercitation veniam in ipsum et nulla.",
                    extra_info="Adipisicing labore culpa commodo eu pariatur enim fugiat eu amet qui. Esse ullamco culpa consequat nisi pariatur eiusmod elit nulla. Duis cillum cillum veniam ullamco deserunt ipsum. Proident sunt reprehenderit cupidatat nisi qui aliqua ea labore enim.",
                )
                course_three.allowed_membership.set(enterprise_membership)
                course_three.instructors.set(third_instructor)
                course_three.save()
        print("Completed!!! Check your database.")
