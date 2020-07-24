from django.urls import path
from .views import TouristSpotDetail, TouristSpotList, TouristSpotPicturesList, TouristSpotPictureDelete

urlpatterns = [
    path('', TouristSpotList.as_view(), name='tourist_spot_list'),
    path('<int:pk>', TouristSpotDetail.as_view()),
    path('<int:id_tourist_point>/pictures', TouristSpotPicturesList.as_view(), name='picture_tourist_spot_list'),
    path('<int:id_tourist_point>/pictures/<int:id_picture>', TouristSpotPictureDelete.as_view()),
]