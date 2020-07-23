from django.test import TestCase


class CategoryTest(TestCase):
    """Test module for Category model"""
    def setUp(self):
        TbCategory.objects.create(name="Categoria 1")
        TbCategory.objects.create(name="Categoria 2")

    def test_category_single(self):
        category = TbCategory.objects.get(pk=1)
        self.assertEquals(category.name, 'Categoria 1')
