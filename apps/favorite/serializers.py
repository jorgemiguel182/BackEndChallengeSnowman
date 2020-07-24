from rest_framework import serializers
from apps.core.models import TbUserFavorite


class UserFavoriteSerializerList(serializers.ModelSerializer):
    class Meta:
        model = TbUserFavorite
        fields = [
            'id',
            'user',
            'tourist_spot'
        ]
