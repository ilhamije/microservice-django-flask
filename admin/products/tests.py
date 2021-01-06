import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from .models import Product
from .serializers import ProductSerializer


# initialize the APIClient App
client = APIClient()


class GetAllProductsTest(TestCase):
    """ Test module to GET all product API """

    def setUp(self):
        Product.objects.create(title="snack 1", image="image item 1")
        Product.objects.create(title="yugurt 2", image="image item 2")
        Product.objects.create(title="coffee 3", image="image item 3")

    def test_get_all_products(self):
        response = client.get(reverse('products-list-create'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(TestCase):
    """ Test module to GET single product API """
    def setUp(self):
        self.snack = Product.objects.create(title="snack", image="image item 1")
        self.yugurt = Product.objects.create(title="yugurt", image="image item 2")
        self.coffee = Product.objects.create(title="coffee", image="image item 3")

    def test_get_valid_single_product(self):
        response = client.get(reverse('products-detail', kwargs={'pk':self.snack.pk}))
        product = Product.objects.get(pk=self.snack.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(reverse('products-detail', kwargs={'pk':91}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            'title': 'Karbol',
            'image': 'Paid karbol'
        }
        self.invalid_payload = {
            'title': '',
            'image': 'Paid karbol'
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('products-list-create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('products-list-create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePuppyTest(TestCase):
    """ Test module for updating an existing product record """

    def setUp(self):
        self.yugurt = Product.objects.create(title="yugurt", image="image item 2")
        self.coffee = Product.objects.create(title="coffee", image="image item 3")
        self.valid_payload = {
            'title': 'Karbol',
            'image': 'Paid karbol'
        }
        self.invalid_payload = {
            'title': '',
            'image': 'Paid karbol'
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('products-detail', kwargs={'pk':self.coffee.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('products-detail', kwargs={'pk':self.coffee.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)