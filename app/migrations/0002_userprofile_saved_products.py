# Generated by Django 5.0 on 2024-10-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saved_products',
            field=models.ManyToManyField(blank=True, to='app.product'),
        ),
    ]