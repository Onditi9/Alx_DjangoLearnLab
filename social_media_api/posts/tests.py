from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostsCommentsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other = User.objects.create_user(username='other', password='otherpass')
        self.post = Post.objects.create(author=self.user, title='Hello', content='World')

    def test_create_post_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('post-list')
        data = {'title': 'New', 'content': 'body'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Post.objects.filter(title='New').count(), 1)

    def test_update_post_by_non_author_forbidden(self):
        self.client.login(username='other', password='otherpass')
        url = reverse('post-detail', args=[self.post.pk])
        resp = self.client.put(url, {'title': 'X', 'content': 'Y'}, format='json')
        self.assertIn(resp.status_code, [403, 405])  # 403 expected

    def test_comment_creation(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('comment-list')
        data = {'post': self.post.pk, 'content': 'Nice post!'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Comment.objects.count(), 1)

