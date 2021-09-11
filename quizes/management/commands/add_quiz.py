from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from quizes.models import Question, Quiz


class Command(BaseCommand):
    help = "Add Quiz to the Database"

    def handle(self, *args, **options):

        for _ in range(3):
            if _ == 0:
                third_lesson = Lesson.objects.filter(
                    title__icontains="Lesson Three"
                ).first()
                Quiz.objects.create(
                    title="Quiz One",
                    description="Dolor aliquip fugiat exercitation veniam in ipsum et nulla.",
                    lesson=third_lesson,
                )

                for _ in range(5):
                    first_quiz = Quiz.objects.filter(
                        title__icontains="Quiz One"
                    ).first()
                    if _ == 0:
                        Question.objects.create(
                            ques="Question One",
                            option1="Option 1",
                            option2="Option 2",
                            option3="Option 3",
                            option4="Option 4",
                            answer="a",
                            quiz=first_quiz,
                        )
                    elif _ == 1:
                        Question.objects.create(
                            ques="Question Two",
                            option1="Option 1",
                            option2="Option 2",
                            option3="Option 3",
                            option4="Option 4",
                            answer="b",
                            quiz=first_quiz,
                        )
                    elif _ == 2:
                        Question.objects.create(
                            ques="Question Three",
                            option1="Option 1",
                            option2="Option 2",
                            option3="Option 3",
                            option4="Option 4",
                            answer="c",
                            quiz=first_quiz,
                        )
                    elif _ == 3:
                        Question.objects.create(
                            ques="Question Four",
                            option1="Option 1",
                            option2="Option 2",
                            option3="Option 3",
                            option4="Option 4",
                            answer="d",
                            quiz=first_quiz,
                        )
                    else:
                        Question.objects.create(
                            ques="Question Five",
                            option1="Option 1",
                            option2="Option 2",
                            option3="Option 3",
                            option4="Option 4",
                            answer="a",
                            quiz=first_quiz,
                        )

        print("Completed!!! Check your database.")
