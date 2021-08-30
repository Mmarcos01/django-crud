
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="test@email.com", password="pass")

        self.snack =Snack.objects.create(
            name="chips", description="cheese", owner=self.user,)

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "chips")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.name}", "chips")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "cheese")
