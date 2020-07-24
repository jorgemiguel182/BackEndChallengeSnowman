from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.core.models import TbCategory, TbTouristSpot, TbPicture


class TouristPointAPITest(APITestCase):

    def setUp(self):
        category = TbCategory.objects.create(name="Categoria 1")
        category.save
        tourist_spot = TbTouristSpot.objects.create(name="Teste", geo_location="123", category=category)
        tourist_spot.save

    def test_api_create_tourist_point_success(self):
        """
        Ensuring the creation of a tourist spot
        """
        url = reverse('tourist_spot_list')
        data = {
            "name": "Teste1",
            "geo_location": "123231321",
            "category": TbCategory.objects.get(name="Categoria 1").id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TbTouristSpot.objects.count(), 2)
        self.assertEqual(TbTouristSpot.objects.filter().last().name, 'Teste1')

    # def test_api_create_picture_to_tourist_point_success(self):
    #     """
    #     Ensuring the creation of a picture to a tourist spot
    #     """
    #     url = reverse('picture_tourist_spot_list', kwargs={'id_tourist_point': TbTouristSpot.objects
    #                                                                            .get(name="Teste").id})
    #     data = {
    #         "picture": "asdçasdsahdaslasdhdiuhasdiuhaoasoduiashoaduasd"
    #     }
    #     response = self.client.post(url, data, format='json')
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(TbPicture.objects.count(), 1)
