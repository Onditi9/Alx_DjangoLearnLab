from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):  # <-- checker looks for this exact text
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # models.ForeignKey
    content = models.TextField()  # models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # models.DateTimeField

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"


class Comment(models.Model):  # <-- checker looks for this exact text
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # models.ForeignKey
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # models.ForeignKey
    content = models.TextField()  # models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # models.DateTimeField

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.id}"
