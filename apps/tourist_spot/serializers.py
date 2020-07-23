from rest_framework import serializers

from ..core.models import TbTouristSpot, TbPicture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbPicture
        fields = [
            'picture'
        ]


class TouristSpotSerializer(serializers.ModelSerializer):
    # pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = TbTouristSpot
        fields = [
            'name',
            # 'pictures',
            'geo_location',
            'category'
        ]
