# Generated by Django 3.0.2 on 2020-01-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20200128_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]