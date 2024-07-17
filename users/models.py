from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import HashedPasswordManager


class User(AbstractUser):
    """
    Модель пользователя, используется для аутентификации
    """
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    username = None
    email = models.EmailField(
        verbose_name='почта',
        help_text="user's email",
        unique=True,
    )

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = HashedPasswordManager()
