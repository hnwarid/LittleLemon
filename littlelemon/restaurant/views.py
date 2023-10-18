from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
from django.contrib.auth.models import User 
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
    

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [IsAuthenticated]



