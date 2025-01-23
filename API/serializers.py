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
    customer = serializers.SlugRelatedField(
        slug_field="telegram_id",
        queryset=CustomUser.objects.all()
    )
    storage_unit = serializers.PrimaryKeyRelatedField(
        queryset=StorageUnit.objects.all(), allow_null=True, required=False
    )
    storage = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Storage.objects.all()
    )

    class Meta:
        model = Order
        fields = (
            'id', 'customer', 'storage_unit', 'storage', 'address', 'phone_number', 'full_name', 'start_date', 'end_date',
            'status', 'qr_issued'
        )
