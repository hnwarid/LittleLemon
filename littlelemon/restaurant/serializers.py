from rest_framework.serializers import ModelSerializer
from .models import Booking, Menu
from django.contrib.auth.models import User 


class MenuSerializer(ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(ModelSerializer):

    class Meta: 
        model = Booking 
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta: 
        model = User
        fields = ['url', 'username', 'email', 'groups']

