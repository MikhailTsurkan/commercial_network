from rest_framework import serializers
from django.contrib.auth import get_user_model

from users import validators

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registration
    """
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password2"]
        validators = [validators.MatchingPasswordsValidator()]
