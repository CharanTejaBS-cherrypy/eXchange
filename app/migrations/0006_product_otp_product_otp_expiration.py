# Generated by Django 5.0 on 2024-10-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='otp_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
