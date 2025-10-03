# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User   # ✅ Required for author field

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ Link to User
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  # ✅ Add published_date

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
