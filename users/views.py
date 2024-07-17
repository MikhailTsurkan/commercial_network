from rest_framework import generics
from users import serializers


class RegistrationAPIView(generics.CreateAPIView):
    """
    Эндпоинт регистрации
    """
    serializer_class = serializers.RegistrationSerializer
