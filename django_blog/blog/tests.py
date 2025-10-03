# blog/tests/test_auth.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_register_view_get(self):
        resp = self.client.get(reverse("register"))
        self.assertEqual(resp.status_code, 200)

    def test_user_registration_and_login(self):
        data = {'username': 'tuser', 'email': 't@example.com', 'password1': 'ComplexPass123', 'password2': 'ComplexPass123'}
        resp = self.client.post(reverse("register"), data, follow=True)
        self.assertContains(resp, "Account created for", status_code=200)

        # try login
        login_resp = self.client.post(reverse("login"), {'username': 'tuser', 'password': 'ComplexPass123'}, follow=True)
        self.assertTrue(login_resp.context['user'].is_authenticated)

