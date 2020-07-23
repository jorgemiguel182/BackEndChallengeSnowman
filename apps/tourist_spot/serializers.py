from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from ..core.models import TbTouristSpot, TbPicture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbPicture
        fields = [
            'picture',
        ]

    # def save(self):


class TouristSpotSerializer(serializers.ModelSerializer):
    # pictures = serializers.RelatedField(read_only=True)
    pictures = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TbTouristSpot
        fields = [
            'id',
            'name',
            'pictures',
            'geo_location',
            'category'
        ]
