# Generated by Django 5.0.6 on 2024-05-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='static\\images'),
        ),
    ]
