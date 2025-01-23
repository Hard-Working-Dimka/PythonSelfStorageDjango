from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telegram_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    telegram_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class Storage(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class StorageUnit(models.Model):
    SIZE_CHOICES = [
        ('small', 'Маленький (до 1 м3)'),
        ('medium', 'Средний (1-5 м3)'),
        ('large', 'Большой (Более 5 м3)'),
    ]

    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name="units")
    unit_number = models.CharField(max_length=50)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.storage.name} - {self.unit_number}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('in_storage', 'In Storage'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.SET_NULL, null=True, blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name="orders")
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_storage')
    qr_issued = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.qr_issued and self.status != 'completed':
            self.status = 'completed'
            if self.storage_unit:
                self.storage_unit.is_occupied = False
                self.storage_unit.save()

        if self.storage_unit and self.status == 'in_storage':
            self.storage_unit.is_occupied = True
            self.storage_unit.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"