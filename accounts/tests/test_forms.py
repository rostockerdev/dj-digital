from django.contrib.auth.models import User
from django.test import TestCase

from accounts.forms import ProfileUpdateForm, UserUpdateForm
from accounts.models import Profile, Subscription
from memberships.models import Membership


class UserUpdateFormTestCase(TestCase):
    def test_user_update_form_fields(self):
        u_form = UserUpdateForm()
        self.assertTrue(u_form.fields["username"].label, "Username:")
        self.assertTrue(u_form.fields["first_name"].label, "First name:")
        self.assertTrue(u_form.fields["last_name"].label, "Last Name:")
        self.assertTrue(u_form.fields["email"].label, "Email address:")


class ProfileUpdateFormTestCase(TestCase):
    def test_profile_update_form_fields(self):
        p_form = ProfileUpdateForm()
        self.assertTrue(p_form.fields["profile_pic"].label, "Profile pic:")
