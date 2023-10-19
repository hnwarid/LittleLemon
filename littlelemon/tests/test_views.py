from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def create_temp_user(self):
        self.temp_user = User.objects.create_user(username='tempuser', password='TEMPp4ss!!!')

    def setUp(self):
        self.create_temp_user()
        self.client = APIClient()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Burger", price=120, inventory=50)
        Menu.objects.create(title="Pizza", price=150, inventory=75)

    def test_getall(self):
        self.client.login(username='tempuser', password='TEMPp4ss!!!')

        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200) 

        expected_data = Menu.objects.all()
        serialized_data = MenuSerializer(expected_data, many=True)
        self.assertEqual(response.data, serialized_data.data)

