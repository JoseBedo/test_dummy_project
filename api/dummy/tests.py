import json
from django.contrib.auth.models import User
from django.test import TestCase, AsyncClient, TransactionTestCase
from rest_framework.test import APIClient, RequestsClient
from asgiref.sync import sync_to_async
# Create your tests here.

class TestRequestAPI(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="usertest", password="passwordtest")
        self.client = APIClient()

    def test_get_hello(self):
        self.client.force_login(user=self.user)
        response = self.client.get('http://localhost:8000/hello/', format='json')
        print(response)
        self.assertEqual(response.status_code, 200) 
    
class TestAsyncTask(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(username="usertest", password="testpassword")
        self.client = AsyncClient()
        self.client.force_login(user=self.user)
    
    async def test_async(self):
        response = await self.client.get('http://localhost:8000/hello/', format='json')
        print(response)
        self.assertEqual(response.status_code, 200)