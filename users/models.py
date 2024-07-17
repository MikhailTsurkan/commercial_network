from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import HashedPasswordManager


class User(AbstractUser):
    """
    Model for users authentication
    """
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    username = None
    email = models.EmailField(
        verbose_name='email',
        help_text="user's email",
        unique=True,
    )

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = HashedPasswordManager()
