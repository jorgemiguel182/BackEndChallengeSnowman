from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..core.models import TbTouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotList(APIView):
    """
    GET - List of registered Tourist Spots
    GET /?name=STRING - Search Tourist Spots by name
    POST - Create a new Tourist Spot
    """
    def get(self, request, format=None):
        tourist_spot = TbTouristSpot.objects.all()
        name = self.request.query_params.get('name')
        if name:
            tourist_spot = TbTouristSpot.objects.filter(name__icontains=name)
        serializer = TouristSpotSerializer(tourist_spot, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TouristSpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TouristSpotDetail(APIView):
    """
    GET + /id - List a Tourist Spot
    PUT + /id - Update a Tourist Spot
    DELETE + /id - Delete a Tourist Spot
    """
    def get_object(self, pk):
        try:
            return TbTouristSpot.objects.get(pk=pk)
        except TbTouristSpot.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tourist_spot = self.get_object(pk)
        serializer = TouristSpotSerializer(tourist_spot)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tourist_spot = self.get_object(pk)
        serializer = TouristSpotSerializer(tourist_spot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tourist_spot = self.get_object(pk)
        tourist_spot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)