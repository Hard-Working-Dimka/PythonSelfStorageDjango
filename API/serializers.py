from rest_framework import serializers
from storage.models import (
    CustomUser, Storage, StorageUnit, Order
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'telegram_id', 'telegram_name')


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('id', 'name', 'location', 'max_capacity')


class StorageUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageUnit
        fields = ('id', 'storage', 'unit_number', 'size', 'is_occupied')


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomUserSerializer()
    storage_unit = StorageUnitSerializer()
    storage = StorageSerializer()

    class Meta:
        model = Order
        depth = 1
        fields = (
            'id', 'customer', 'storage_unit', 'storage', 'address', 'phone_number', 'full_name', 'start_date', 'end_date',
            'status', 'qr_issued'
        )
