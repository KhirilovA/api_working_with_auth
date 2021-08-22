from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
from cars.permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )