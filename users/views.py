from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users import serializers


class RegistrationAPIView(generics.CreateAPIView):
    """
    Эндпоинт регистрации
    """
    permission_classes = [~IsAuthenticated]
    serializer_class = serializers.RegistrationSerializer
