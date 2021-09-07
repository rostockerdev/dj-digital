import datetime
import random

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse

from accounts.forms import ProfileUpdateForm, UserUpdateForm
from instructors.models import Instructor


class ProfileViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Create 3 Instructors
        no_of_instructors = 3
        for i in range(no_of_instructors):
            Instructor.objects.create(
                username=f"instructor{i}",
                first_name=f"first{i}",
                last_name=f"last{i}",
                email=f"first_last{i}@gmail.com",
                dofb=datetime.date.today() - datetime.timedelta(days=5),
                biography=f"biography{i}",
            )
        cls.test_user = User.objects.create_user(
            username="test_user", password="test_pass"
        )
        cls.test_user.save()

    def test_profile_view_with_anonymous_user_url(self):
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/profile/")

    def test_profile_view_with_login_user_url(self):
        self.client.login(username="test_user", password="test_pass")
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")

    def test_profile_view(self):
        self.client.login(username="test_user", password="test_pass")
        response = self.client.get(reverse("profile"))
        u_form_data = {
            "username": "test_user2",
            "first_name": "test",
            "last_name": "user2",
            "email": "test_user2@gmail.com",
        }
        u_form = UserUpdateForm(u_form_data)
        # print(u_form)
        self.assertTrue(u_form.is_valid())
        p_form = ProfileUpdateForm({"profile_pic": "avatar.jpg"})
        self.assertTrue(p_form.is_valid())
        # self.assertRedirects(response, 'memberships:dashboard')
        # self.assertRedirects(response, 'memberships:dashboard')
        instructors = Instructor.objects.order_by("dofb").all()[:3]
        self.assertEqual(instructors.count(), 3)
        self.assertTrue(
            "u_form" in response.context,
        )
        self.assertTrue(
            "p_form" in response.context,
        )
        self.assertTemplateUsed(response, "accounts/profile.html")
