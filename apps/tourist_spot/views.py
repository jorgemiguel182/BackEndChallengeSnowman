from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tourist_spot.utils import search_tourist_spots_in_radius
from ..core.models import TbTouristSpot, TbPicture
from .serializers import TouristSpotSerializer, PictureSerializer


class TouristSpotList(APIView):
    """
    GET - List of registered Tourist Spots + pictures (pictures is read/download only )
    GET /?name=STRING - Search Tourist Spots by name
    POST - Create a new Tourist Spot
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    name = openapi.Parameter('name', openapi.IN_QUERY, description="name", type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[name],
        responses={'200': 'Ok', '400': "Bad Request"},
        operation_description='GET - List of registered Tourist Spots + pictures (pictures is read/download only ) '
                              '\n GET /?name=STRING - Search Tourist Spots by name',
    )
    def get(self, request, format=None):
        tourist_spot = TbTouristSpot.objects.all()
        name = self.request.query_params.get('name')
        if name:
            tourist_spot = TbTouristSpot.objects.filter(name__icontains=name)
        serializer = TouristSpotSerializer(tourist_spot, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=TouristSpotSerializer,
        responses={'201': 'Created', '400': "Bad Request"},
        operation_description='POST - Create a new Tourist Spot',
    )
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

    @swagger_auto_schema(
        responses={'200': 'Ok', '400': "Bad Request"},
        operation_description='GET + /id - Get a Tourist Spot + pictures (pictures is read/download only)',
    )
    def get(self, request, pk, format=None):
        tourist_spot = self.get_object(pk)
        serializer = TouristSpotSerializer(tourist_spot, context={"request": request})
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=TouristSpotSerializer,
        responses={'200': 'Ok', '400': "Bad Request"},
        operation_description='PUT + /id - Update a Tourist Spot',
    )
    def put(self, request, pk, format=None):
        tourist_spot = self.get_object(pk)
        serializer = TouristSpotSerializer(tourist_spot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={'204': 'No Content', '400': "Bad Request"},
        operation_description='GET + /id - Get a Tourist Spot + pictures (pictures is read/download only)',
    )
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

    @swagger_auto_schema(
        responses={'200': 'Ok', '400': "Bad Request"},
        operation_description='GET - List of registered Pictures of a Tourist Spot',
    )
    def get(self, request, id_tourist_point, format=None):
        pictures = self.get_object(id_tourist_point)
        serializer = PictureSerializer(pictures, many=True, context={"request": request})
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=PictureSerializer,
        responses={'201': 'Created', '400': "Bad Request"},
        operation_description='POST - Register a new Picture to a Tourist Spots',
    )
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

    @swagger_auto_schema(
        responses={'204': 'No Content', '400': "Bad Request"},
        operation_description='DELETE + /id_picture- Delete a Picture',
    )
    def delete(self, request, id_tourist_point, id_picture, format=None):
        picture = self.get_object(id_picture)
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TouristSpotBy5KMRadius(APIView):
    """
    GET + ?address=STRING & city=STRING & state=STRING & lat=STRING & long=STRING
        - Will return a list of tourist spots within a 5km radius
    """
    permission_classes = [permissions.AllowAny]

    address = openapi.Parameter('address', openapi.IN_QUERY, description="name", type=openapi.TYPE_STRING)
    city = openapi.Parameter('city', openapi.IN_QUERY, description="city", type=openapi.TYPE_STRING)
    state = openapi.Parameter('state', openapi.IN_QUERY, description="state", type=openapi.TYPE_STRING)
    lat = openapi.Parameter('lat', openapi.IN_QUERY, description="lat", type=openapi.TYPE_STRING)
    long = openapi.Parameter('long', openapi.IN_QUERY, description="long", type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[address, city, state, lat, long],
        responses={'200': 'Ok', '400': "Bad Request"},
        operation_description='GET + ?address=STRING & city=STRING & state=STRING & lat=STRING & long=STRING '
                              '\n - Will return a list of tourist spots within a 5km radius',
    )
    def get(self, request, format=None):
        address = self.request.query_params.get('address')
        city = self.request.query_params.get('city')
        state = self.request.query_params.get('state')
        lat = self.request.query_params.get('lat')
        long = self.request.query_params.get('long')

        tourist_spots = search_tourist_spots_in_radius(distance=6,
                                                       address=address,
                                                       city=city,
                                                       state=state,
                                                       lat=lat,
                                                       long=long)
        serializer = TouristSpotSerializer(tourist_spots, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
