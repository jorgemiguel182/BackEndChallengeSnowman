from django.urls import path

from apps.auth_user.views import UserCreate, ObtainAuthToken

urlpatterns = [
    path('token', ObtainAuthToken.as_view()),
    path('new', UserCreate.as_view()),
]
