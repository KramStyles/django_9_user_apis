import time

from django.urls import reverse
from rest_framework.test import APITestCase


class TestTodoList(APITestCase):
    start = None

    @classmethod
    def setUpClass(cls):
        cls.start = time.time()

    def authenticate_user(self):
        self.client.post(reverse('register'), {'username': "username", 'password': "password",
                                               'email': "mail@email.com"})
        response = self.client.post(reverse('login'), {'password': 'password', 'email': 'mail@email.com'})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

    def test_to_throw_error_on_create_todo_with_no_authentication(self):
        sample_todo = {'title': 'hello', 'desc': 'testing'}
        response = self.client.post(reverse('list-create-todo'), sample_todo)
        self.assertEqual(response.status_code, 403)

    def test_to_create_todo_with_authentication(self):
        self.authenticate_user()
        sample_todo = {'title': 'hello', 'desc': 'testing'}
        response = self.client.post(reverse('list-create-todo'), sample_todo)
        self.assertEqual(response.status_code, 201)

    @classmethod
    def tearDownClass(cls):
        print('Total time to test Authentication:', time.time() - cls.start)
