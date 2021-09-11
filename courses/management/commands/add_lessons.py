from django.core.management.base import BaseCommand

from courses.models import Course, Lesson


class Command(BaseCommand):
    help = "Add Lessons to the Database"

    def handle(self, *args, **options):

        for _ in range(3):
            if _ == 0:
                first_course = Course.objects.filter(
                    title__icontains="Course One"
                ).first()
                Lesson.objects.create(
                    title="Lesson One",
                    description="Dolor aliquip fugiat exercitation veniam in ipsum et nulla.",
                    extra_info="Adipisicing labore culpa commodo eu pariatur enim fugiat eu amet qui. Esse ullamco culpa consequat nisi pariatur eiusmod elit nulla. Duis cillum cillum veniam ullamco deserunt ipsum. Proident sunt reprehenderit cupidatat nisi qui aliqua ea labore enim.",
                    course=first_course,
                )

            elif _ == 1:
                second_course = Course.objects.filter(
                    title__icontains="Course Two"
                ).first()
                Lesson.objects.create(
                    title="Lesson Two",
                    description="Dolor aliquip fugiat exercitation veniam in ipsum et nulla.",
                    extra_info="Adipisicing labore culpa commodo eu pariatur enim fugiat eu amet qui. Esse ullamco culpa consequat nisi pariatur eiusmod elit nulla. Duis cillum cillum veniam ullamco deserunt ipsum. Proident sunt reprehenderit cupidatat nisi qui aliqua ea labore enim.",
                    course=second_course,
                )
            elif _ == 2:
                third_course = Course.objects.filter(
                    title__icontains="Course Three"
                ).first()
                Lesson.objects.create(
                    title="Lesson Three",
                    description="Dolor aliquip fugiat exercitation veniam in ipsum et nulla.",
                    extra_info="Adipisicing labore culpa commodo eu pariatur enim fugiat eu amet qui. Esse ullamco culpa consequat nisi pariatur eiusmod elit nulla. Duis cillum cillum veniam ullamco deserunt ipsum. Proident sunt reprehenderit cupidatat nisi qui aliqua ea labore enim.",
                    course=third_course,
                )
        print("Completed!!! Check your database.")
