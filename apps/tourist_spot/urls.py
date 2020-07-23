from django.urls import path
from .views import TouristSpotDetail, TouristSpotList

urlpatterns = [
    path('', TouristSpotList.as_view()),
    path('<int:pk>', TouristSpotDetail.as_view()),
]