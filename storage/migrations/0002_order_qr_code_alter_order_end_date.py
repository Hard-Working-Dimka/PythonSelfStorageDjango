# Generated by Django 5.1.1 on 2025-01-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
