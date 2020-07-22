from rest_framework import serializers

from SnowManAPI.apps.core.models import TbCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCategory
        fields = [
            'name'
        ]