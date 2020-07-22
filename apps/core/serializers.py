from rest_framework import serializers

from .models import TbCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCategory
        fields = [
            'name'
        ]