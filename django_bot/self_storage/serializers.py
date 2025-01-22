from rest_framework import serializers
from .models import (
    Client, Warehouse, Plans, Order
)


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# class ClientsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         field = '__all__'
#
# class ClientsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         field = '__all__'