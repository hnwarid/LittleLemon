from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_items(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # self.assertEqual(item, "IceCream : 80")
        expected_string = f'{item.title} : {str(item.price)}'
        self.assertEqual(str(item), expected_string)