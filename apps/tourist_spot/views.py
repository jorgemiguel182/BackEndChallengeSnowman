from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..core.models import TbTouristSpot, TbPicture
from .serializers import TouristSpotSerializer, PictureSerializer


class TouristSpotList(APIView):
    """
    GET - List of registered Tourist Spots + pictures (pictures is read/download only )
    GET /?name=STRING - Search Tourist Spots by name
    POST - Create a new Tourist Spot
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        tourist_spot = TbTouristSpot.objects.all()
        name = self.request.query_params.get('name')
        if name:
            tourist_spot = TbTouristSpot.objects.filter(name__icontains=name)
        serializer = TouristSpotSerializer(tourist_spot, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TouristSpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TouristSpotDetail(APIView):
    """
    GET + /id - Get a Tourist Spot + pictures (pictures is read/download only )
    PUT + /id - Update a Tourist Spot
    DELETE + /id - Delete a Tourist Spot
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return TbTouristSpot.objects.get(pk=pk)
        except TbTouristSpot.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tourist_spot = self.get_object(pk)
        serializer = TouristSpotSerializer(tourist_spot, context={"request": request})
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


class TouristSpotPicturesList(APIView):
    """
    GET - List of registered Pictures of a Tourist Spot
    POST - Register a new Picture to a Tourist Spots
    DELETE + /id_picture - Delete a Picture
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, id_tourist_point):
        try:
            TbTouristSpot.objects.get(pk=id_tourist_point)
            return TbPicture.objects.filter(tourist_spot=id_tourist_point)
        except TbTouristSpot.DoesNotExist:
            raise Http404

    def get(self, request, id_tourist_point, format=None):
        pictures = self.get_object(id_tourist_point)
        serializer = PictureSerializer(pictures, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, id_tourist_point, format=None):
        request.data['tourist_spot_id'] = id_tourist_point
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TouristSpotPictureDelete(APIView):
    """
    DELETE - Delete a Picture
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id_picture):
        try:
            return TbPicture.objects.get(pk=id_picture)
        except TbPicture.DoesNotExist:
            raise Http404

    def delete(self, request, id_tourist_point, id_picture, format=None):
        picture = self.get_object(id_picture)
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
