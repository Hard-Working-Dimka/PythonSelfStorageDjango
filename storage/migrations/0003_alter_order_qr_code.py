# Generated by Django 5.1.1 on 2025-01-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_order_qr_code_alter_order_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
    ]
