# Generated by Django 3.0.2 on 2020-02-07 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_orderproduct_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
    ]