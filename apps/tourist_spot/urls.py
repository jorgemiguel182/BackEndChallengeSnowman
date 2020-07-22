from django.urls import include, path
from rest_framework import routers
# from .views import CategoryView
#
# app_name = "category"
# api_router = routers.DefaultRouter()
# api_router.register(r'', CategoryView)
from ..tourist_spot.views import TouristSpotDetail, TouristSpotList

urlpatterns = [
    path('', TouristSpotList.as_view()),
    path('(?P<name>.+)', TouristSpotList.as_view()),
    path('<int:pk>', TouristSpotDetail.as_view()),
]