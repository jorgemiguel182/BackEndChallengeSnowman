from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import TbUserFavorite
from apps.favorite.serializers import UserFavoriteSerializerList


class UserFavoriteList(APIView):
    """
    GET + /user_id - Get a list of tourist spot favorites for a User
    POST + /user_id - Add a Favorite Tourist Point to a user (data={user:INT, tourist_spot:INT})
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object_list(self, pk):
        try:
            favs = TbUserFavorite.objects.filter(user=pk)
            if not favs:
                raise Http404
            return favs
        except TbUserFavorite.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        manual_parameters=[],
        responses={'200': 'Ok', '400': "Bad Request"},
        operation_description='GET + /user_id - Get a list of tourist spot favorites for a User',
    )
    def get(self, request, user_id, format=None):
        favs = self.get_object_list(user_id)
        serializer = UserFavoriteSerializerList(favs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserFavoriteSerializerList,
        responses={'200': 'Ok', '400': "Bad Request"},
        operation_description='POST + /user_id - Add a Favorite Tourist Point to a user (data={user:INT, '
                              'tourist_spot:INT})',
    )
    def post(self, request, user_id, format=None):
        serializer = UserFavoriteSerializerList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFavoriteDetail(APIView):
    """
    DELETE + /<user_id>/touris-spot-favorite/<tourist_spot_id> - Delete a favorited row of a tourist point
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user_id, tourist_spot_id):
        try:
            return TbUserFavorite.objects.get(user__id=user_id, tourist_spot__id=tourist_spot_id)
        except TbUserFavorite.DoesNotExist:
            raise Http404


    @swagger_auto_schema(
        manual_parameters=[],
        responses={'204': 'No Content', '400': "Bad Request"},
        operation_description='DELETE + /<user_id>/touris-spot-favorite/<tourist_spot_id> - Delete a favorited row of '
                              'a tourist point',
    )
    def delete(self, request, user_id, tourist_spot_id, format=None):
        favorited_spot = self.get_object(user_id, tourist_spot_id)
        favorited_spot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
