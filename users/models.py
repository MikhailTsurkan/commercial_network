from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

from users.managers import HashedPasswordManager


class User(AbstractUser):
    """
    Model for users authentication
    """
    class Meta:
        verbose_name = gettext_lazy('User')
        verbose_name_plural = gettext_lazy('Users')

    username = None
    email = models.EmailField(
        verbose_name=gettext_lazy('email'),
        help_text=gettext_lazy("user's email"),
        unique=True,
    )

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = HashedPasswordManager()
