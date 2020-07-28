from django.urls import path
from .views import TouristSpotDetail, TouristSpotList, TouristSpotPicturesList, TouristSpotPictureDelete, \
TouristSpotBy5KMRadius

urlpatterns = [
    # Tourist Spot
    path('', TouristSpotList.as_view(), name='tourist_spot_list'),
    path('<int:pk>', TouristSpotDetail.as_view()),

    # Pictures of Tourist Spot
    path('<int:id_tourist_point>/pictures', TouristSpotPicturesList.as_view(), name='picture_tourist_spot_list'),
    path('<int:id_tourist_point>/pictures/<int:id_picture>', TouristSpotPictureDelete.as_view()),

    # Search Tourist Spot in a 5km radius, by address
    path('by_radius_5km', TouristSpotBy5KMRadius.as_view()),
]