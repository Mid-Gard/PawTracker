# Generated by Django 4.2 on 2023-04-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_details', '0003_rename_phonenumber_driver_details_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_details',
            name='Phone_Number',
            field=models.IntegerField(),
        ),
    ]
