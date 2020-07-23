from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from ..core.models import TbTouristSpot, TbPicture


class PictureSerializer(serializers.ModelSerializer):
    # user = PrimaryKeyRelatedField(1,2,3)

    class Meta:
        model = TbPicture
        fields = [
            'picture'
        ]

    # def save(self):

class TouristSpotSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = TbTouristSpot
        fields = [
            'name',
            'pictures',
            'geo_location',
            'category'
        ]
