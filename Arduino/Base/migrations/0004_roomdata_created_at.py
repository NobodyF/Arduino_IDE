# Generated by Django 4.2.19 on 2025-02-15 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_alter_roomdata_humidity_alter_roomdata_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
