# Generated by Django 3.0.2 on 2020-01-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200127_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
