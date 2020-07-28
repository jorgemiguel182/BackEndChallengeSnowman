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
    # lat = serializers.CharField(max_length=50, required=False, allow_blank=False, allow_null=True)
    # long = serializers.CharField(max_length=50, required=False, allow_blank=False, allow_null=True)

    class Meta:
        model = TbTouristSpot
        fields = [
            'id',
            'name',
            'pictures',
            'address',
            'state',
            'country',
            # 'lat',
            # 'long',
            'category'
        ]
