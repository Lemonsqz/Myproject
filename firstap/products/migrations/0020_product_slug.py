# Generated by Django 3.0.2 on 2020-02-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='test_product'),
            preserve_default=False,
        ),
    ]
