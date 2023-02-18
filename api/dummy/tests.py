import json
from django.test import TestCase
from rest_framework.test import APIClient, RequestsClient
# Create your tests here.

class TestRequestAPI(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_hello(self):
        response = self.client.get('http://localhost:8000/hello/', format='json')
        print(response)
        self.assertEqual(response.status_code, 200) 
    
