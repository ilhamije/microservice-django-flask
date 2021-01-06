from django.test import TestCase
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        p = Product.objects.create(title="title test", image="image test")
        self.test_product_id = p.pk

    def test_get_product(self):
        title = Product.objects.get(title="title test")
        self.assertEquals(title.image, 'image test')

    def test_get_one_product(self):
        title = Product.objects.get(pk=self.test_product_id)
        self.assertEquals(title.image, 'image test')
