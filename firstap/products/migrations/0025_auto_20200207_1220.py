# Generated by Django 3.0.2 on 2020-02-07 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_orderproduct_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
