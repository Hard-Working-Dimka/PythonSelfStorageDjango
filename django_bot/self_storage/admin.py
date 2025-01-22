from django.contrib import admin
from .models import (
    Client, Warehouse, Plans, Order
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address_of_client')


@admin.register(Warehouse)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('address', 'free_capacity')


@admin.register(Plans)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('volume_of_cell', 'price')


@admin.register(Order)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'cell_address', 'days', 'size', 'delivery', 'days_left', 'key_of_cell', 'plan', 'items'
    )
