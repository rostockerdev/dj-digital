from django.core.management.base import BaseCommand

from instructors.models import Instructor


class Command(BaseCommand):
    help = "Add instructors to the Database"

    def handle(self, *args, **options):

        for _ in range(3):
            if _ == 0:
                Instructor.objects.create(
                    username="instructorone",
                    first_name="instructor",
                    last_name="one",
                    email="raselrostock@yahoo.com",
                    dofb="1985-11-12",
                    biography="Irure non non voluptate sint nulla consectetur proident consequat veniam deserunt non. Ut pariatur ea nostrud deserunt commodo reprehenderit non laborum occaecat eiusmod laboris nisi incididunt. Officia fugiat elit veniam dolore. Voluptate pariatur officia aliquip magna sit cupidatat reprehenderit in esse dolor. Cillum voluptate est qui exercitation magna cillum consectetur adipisicing voluptate proident et velit.",
                    pro_pic="jenny.jpg",
                )
            elif _ == 1:
                Instructor.objects.create(
                    username="instructortwo",
                    first_name="instructor",
                    last_name="two",
                    email="instructortwo@yahoo.com",
                    dofb="1990-10-10",
                    biography="Excepteur incididunt ea aliqua ad ipsum ad cupidatat nulla. Tempor quis esse occaecat voluptate do incididunt dolor et occaecat ea nisi eu anim nostrud. Mollit non reprehenderit ipsum Lorem. Exercitation incididunt consectetur eu Lorem do esse elit dolor elit veniam nulla sunt.",
                    pro_pic="jenny.jpg",
                )
            elif _ == 2:
                Instructor.objects.create(
                    username="instructorthree",
                    first_name="instructor",
                    last_name="three",
                    email="instructorthree@yahoo.com",
                    dofb="1995-01-01",
                    biography="Irure non non voluptate sint nulla consectetur proident consequat veniam deserunt non. Ut pariatur ea nostrud deserunt commodo reprehenderit non laborum occaecat eiusmod laboris nisi incididunt. Officia fugiat elit veniam dolore. Voluptate pariatur officia aliquip magna sit cupidatat reprehenderit in esse dolor. Cillum voluptate est qui exercitation magna cillum consectetur adipisicing voluptate proident et velit.",
                    pro_pic="jenny.jpg",
                )

        print("Completed!!! Check your database.")
