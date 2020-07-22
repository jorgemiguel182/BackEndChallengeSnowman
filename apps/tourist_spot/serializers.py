from rest_framework import serializers

from ..core.models import TbTouristSpot, TbPicture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbPicture
        fields = [
            'picture'
        ]


class TouristSpotSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True)

    class Meta:
        model = TbTouristSpot
        fields = [
            'name',
            'pictures',
            'geo_location',
            'category'
        ]

    def create(self, validated_data):
        images = validated_data.pop('pictures')
        spots = TbTouristSpot.objects.create(**validated_data)
        for i in images:
            TbPicture.objects.create(TbTouristSpot=images, **i)
        return spots