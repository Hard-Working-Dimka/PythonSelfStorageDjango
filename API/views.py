from rest_framework import viewsets

from storage.models import (
    CustomUser, Storage, StorageUnit, Order
)
from API.serializers import (
    CustomUserSerializer, StorageSerializer, StorageUnitSerializer, OrderSerializer
)


class CustomUserApiView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class StorageApiView(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageUnitApiView(viewsets.ModelViewSet):
    queryset = StorageUnit.objects.all()
    serializer_class = StorageUnitSerializer


class OrderApiView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
