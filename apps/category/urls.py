from django.urls import include, path
from rest_framework import routers
from .views import CategoryView

app_name = "category"
api_router = routers.DefaultRouter()
api_router.register(r'', CategoryView)

urlpatterns = [
    path("/", include(api_router.urls)),
]