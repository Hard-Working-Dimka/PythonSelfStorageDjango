from django.contrib import admin
from .models import CustomUser, Storage, StorageUnit, Order


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telegram_id', 'telegram_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'telegram_id', 'telegram_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'max_capacity', 'available_units')
    search_fields = ('name', 'location')
    list_filter = ('location',)

    def available_units(self, obj):
        return obj.units.filter(is_occupied=False).count()
    available_units.short_description = 'Available Units'


@admin.register(StorageUnit)
class StorageUnitAdmin(admin.ModelAdmin):
    list_display = ('unit_number', 'storage', 'size', 'is_occupied')
    search_fields = ('unit_number', 'storage__name', 'size')
    list_filter = ('is_occupied', 'storage')
    list_editable = ('is_occupied',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'storage', 'status', 'start_date', 'end_date', 'qr_issued')
    list_filter = ('status', 'storage', 'qr_issued')
    search_fields = ('customer__username', 'storage__name')
    list_editable = ('status', 'qr_issued')

