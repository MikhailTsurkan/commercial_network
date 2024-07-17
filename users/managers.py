from django.contrib.auth.hashers import make_password
from django.db.models import Manager


class HashedPasswordManager(Manager):
    """
    Менеджер модели User, позволяющий хранить пароли в зашифрованном виде
    """
    def create(self, email, password, **kwargs):
        user = super().create(email=email, password=make_password(password), **kwargs)
        return user
