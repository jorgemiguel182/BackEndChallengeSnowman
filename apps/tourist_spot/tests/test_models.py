from django.test import TestCase

from apps.core.models import TbTouristSpot, TbCategory


class TouristPointModelTest(TestCase):
    """Test module for TouristPoint model"""
    def setUp(self):
        category = TbCategory.objects.create(name="Categoria 1")
        category.save
        TbTouristSpot.objects.create(name="Teste1", geo_location="123", category=category)

    def test_category_single(self):
        tourist_spot = TbTouristSpot.objects.filter().first()
        self.assertEquals(tourist_spot.name, 'Teste1')
