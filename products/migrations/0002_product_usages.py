# Generated by Django 5.1.4 on 2025-05-22 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='usages',
            field=models.ManyToManyField(to='products.productusage'),
        ),
    ]
