# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True,
        help_text='Users that this user follows'
    )

    def follow(self, user):
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(pk=user.pk).exists()

    def __str__(self):
        return self.username