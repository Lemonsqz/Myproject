# Generated by Django 2.2.2 on 2019-07-29 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20190725_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='rifle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Rifle'),
        ),
    ]
