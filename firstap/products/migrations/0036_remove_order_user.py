# Generated by Django 3.0.2 on 2020-02-11 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_order_ordered_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]