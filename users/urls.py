from django.urls import path
from rest_framework_simplejwt.views import token_refresh, token_obtain_pair
from users.views import RegistrationAPIView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("token/obtain/", token_obtain_pair, name="token-obtain-pair"),
    path("token/refresh/", token_refresh, name="token-refresh"),

    path("register/", RegistrationAPIView.as_view(), name="register"),
]
