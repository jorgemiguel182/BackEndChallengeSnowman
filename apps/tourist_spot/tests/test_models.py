from django.contrib.auth.models import User
from django.test import TestCase

from apps.core.models import TbTouristSpot, TbCategory, TbUserFavorite


class TouristPointModelsTest(TestCase):
    """Test module for TouristPoint model and correlations"""
    def setUp(self):
        user = User.objects.create(password='test@123', username='teste_api', email='teste@teste.com')
        category = TbCategory.objects.create(name="Categoria 1")
        v_tourist_spot = TbTouristSpot.objects.create(name="Teste1", address="Rua tal, n50", state='MG',
                                                      category=category)
        TbUserFavorite.objects.create(tourist_spot=v_tourist_spot, user=user)

    def test_category_single(self):
        caregory = TbCategory.objects.filter().first()
        self.assertEquals(caregory.name, 'Categoria 1')

    def test_tourist_spot_single(self):
        tourist_spot = TbTouristSpot.objects.filter().first()
        self.assertEquals(tourist_spot.name, 'Teste1')

    def test_user_favorite_single(self):
        user_favorite = TbUserFavorite.objects.filter().first()
        self.assertEquals(user_favorite.user.username, 'teste_api')
