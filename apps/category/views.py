from rest_framework import viewsets

from ..core.models import TbCategory
from ..core.serializers import CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    '''
    GET - List of registered categories
    POST - Create a new category
    GET + /id - List a category
    PUT + /id - Update a category
    DELETE + /id - Delete a category
    '''
    queryset = TbCategory.objects.all()
    serializer_class = CategorySerializer
