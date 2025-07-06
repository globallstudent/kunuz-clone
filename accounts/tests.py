from django.test import TestCase
from accounts.models import User


class UserManagerTests(TestCase):
    def test_create_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password="secret")
