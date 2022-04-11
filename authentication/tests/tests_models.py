from time import time

from rest_framework.test import APITestCase

from authentication.models import User


class TestModels(APITestCase):
    start_time = None

    @classmethod
    def setUpClass(cls):
        cls.start_time = time()

    def test_if_user_is_created(self):
        user = User.objects.create_user('kramstyles', 'kramstyles@outlook.com', 'pass1234')

        self.assertEqual(user.username, 'kramstyles')
        self.assertFalse(user.is_staff)
        self.assertIsInstance(user, User)

    def test_if_superuser_is_created(self):
        user = User.objects.create_superuser('kramstyles', 'kramstyles@outlook.com', 'pass1234')

        self.assertEqual(user.username, 'kramstyles')
        self.assertTrue(user.is_staff)
        self.assertIsInstance(user, User)

    def test_for_token(self):
        self.assertEqual(User().token, 'token')

    def test_if_username_and_email_are_missing(self):
        with self.assertRaises(TypeError):
            user = User.objects.create_user()

        with self.assertRaises(ValueError):
            user = User.objects.create_user(None, None)

        with self.assertRaises(ValueError):
            User.objects.create_user('kramstyles', None)

    def test_if_staff_and_super_status_is_missing(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser('username', 'user@mail.com', is_staff=False)

        with self.assertRaises(ValueError):
            User.objects.create_superuser('username', 'user@mail.com', is_superuser=False)

    @classmethod
    def tearDownClass(cls):
        print("Time taken to run this:", time() - cls.start_time)
