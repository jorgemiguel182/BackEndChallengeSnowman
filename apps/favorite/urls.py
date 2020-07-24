from django.urls import path

from apps.favorite.views import UserFavoriteList, UserFavoriteDetail

urlpatterns = [
    path('<int:user_id>/', UserFavoriteList.as_view(), name='user_favorite_list'),
    path('<int:user_id>/touris-spot-favorite/<int:tourist_spot_id>', UserFavoriteDetail.as_view())
]