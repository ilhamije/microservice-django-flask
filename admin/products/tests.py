from django.test import TestCase
from .models import Product
from .serializers import ProductSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


# initialize the APIClient App
client = APIClient()


class GetAllProductsTest(TestCase):
    def setUp(self):
        Product.objects.create(title="title test 1", image="image test 1")
        Product.objects.create(title="title test 2", image="image test 2")
        Product.objects.create(title="title test 3", image="image test 3")

    def test_get_all_products(self):
        response = client.get(reverse('products-list-create'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


