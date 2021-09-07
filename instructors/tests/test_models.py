# from django.contrib.auth.models import User
# from django.test import TestCase
# from django.urls.base import reverse

# from instructors.models import Instructor, Rating


# class InstructorModelTestCase(TestCase):
#     @classmethod
#     def setUpTestData(cls) -> None:
#         test_instructor = Instructor.objects.create(
#             username="mostofa kamal",
#             first_name="mostofa",
#             last_name="kamal",
#             email="mostofa.kamal@gmail.com",
#         )
#         test_user = User.objects.create_user(username="testuser", password="password")
#         # test_rating = Rating.objects.create(
#         #     instructor=test_instructor, user=test_user, review="review", rating="1"
#         # )

#     def test_name_labels(self):
#         test_instructor = Instructor.objects.get(id=1)
#         first_name_label = test_instructor._meta.get_field("first_name").verbose_name
#         last_name_label = test_instructor._meta.get_field("last_name").verbose_name
#         self.assertEqual(first_name_label, "First Name")
#         self.assertEqual(last_name_label, "Last Name")

#     def test_instructor_correct_object(self):
#         test_instructor = Instructor.objects.get(id=1)
#         self.assertEqual(str(test_instructor), "mostofa kamal")

#     def test_get_absolute_url(self):
#         test_instructor = Instructor.objects.get(id=1)
#         response = self.client.get(
#             reverse(
#                 "instructors:instructor-detail",
#                 kwargs={"instructor_name": test_instructor.username},
#             )
#         )
#         self.assertEqual(response.status_code, 200)

#     # def test_instructor_rating(self):
#     #     test_instructor = Instructor.objects.get(id=1)
#     #     test_rating = Rating.objects.filter(instructor=test_instructor)
#     #     print(test_rating)
