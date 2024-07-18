from django.utils.translation import gettext_lazy
from rest_framework.exceptions import ValidationError


class MatchingPasswordsValidator:
    """
    Validator for checking of matching password and password2 fields
    """
    message = gettext_lazy("Passwords must match")

    def __call__(self, value):
        password1 = value.get("password")
        password2 = value.pop("password2", None)

        if password1 != password2:
            raise ValidationError(self.message)
