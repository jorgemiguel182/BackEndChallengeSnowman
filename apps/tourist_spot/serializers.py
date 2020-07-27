from rest_framework import serializers
from ..core.models import TbTouristSpot, TbPicture


class PictureSerializer(serializers.ModelSerializer):
    tourist_spot_id = serializers.IntegerField()
    picture = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = TbPicture
        fields = [
            'id',
            'picture',
            'tourist_spot_id'
        ]


class TouristSpotSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = TbTouristSpot
        fields = [
            'id',
            'name',
            'pictures',
            'geo_location',
            'category'
        ]
