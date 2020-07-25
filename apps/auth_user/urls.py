from django.urls import path
from rest_framework.authtoken import views

from apps.auth_user.views import UserCreate

urlpatterns = [
    path('token', views.obtain_auth_token),
    path('new', UserCreate.as_view()),
]
