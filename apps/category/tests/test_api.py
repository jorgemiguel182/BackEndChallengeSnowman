# from django.test import TestCase
#
# # Create your tests here.
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
#
# print('1111111')
# class CategoryTest(APITestCase):
#     print('2222222')
#
#     def test_create_category(self):
#         """
#         Garantindo a criação de uma categoria
#         """
#         url = reverse('categ')
#         data = {
#             'name': 'Praça A'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         from SnowManAPI.apps.core.models import TbCategory
#         self.assertEqual(TbCategory.objects.count(), 1)
#         self.assertEqual(TbCategory.objects.get().name, 'Praça A')