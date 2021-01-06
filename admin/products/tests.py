from django.test import TestCase
from .models import Product
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ProductTestCase(TestCase):
    def setUp(self):
        p = Product.objects.create(title="title test", image="image test")
        self.test_product_id = p.pk

    def test_get_product(self):
        title = Product.objects.get(title="title test")
        self.assertEquals(title.image, 'image test')

    def test_get_one_product(self):
        product = Product.objects.get(pk=self.test_product_id)
        self.assertEquals(product.image, 'image test')

    # def test_update_one_product(self):
    #     product = Product.objects.get(pk=self.test_product_id)
    #     updated_product = Product.objects.update(image='image updated')
    #     self.assertEquals(updated_product.image, 'image updated')


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.productlist_data = {
            'title':'product api test',
            'image':'imagine the future'
            }
        self.response = self.client.post(
            reverse('products-list-create'),
            self.productlist_data,
            format='json'
        )

    def test_api_create_product(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)