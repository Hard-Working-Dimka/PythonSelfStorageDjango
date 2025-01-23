from rest_framework import serializers
from storage.models import (
    CustomUser, Storage, StorageUnit, Order
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class StorageUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageUnit
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
