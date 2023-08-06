# Generated by Django 4.2 on 2023-04-15 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_remove_locationdata_bus2_lon_locationdata_bus1_lng_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus1_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus1_lat', models.FloatField()),
                ('bus1_lng', models.FloatField()),
                ('bus1_time', models.DateTimeField()),
                ('bus1_date', models.DateTimeField()),
                ('bus1_speed', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bus2_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus2_lat', models.FloatField()),
                ('bus2_lng', models.FloatField()),
                ('bus2_time', models.DateTimeField()),
                ('bus2_date', models.DateTimeField()),
                ('bus2_speed', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bus3_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus3_lat', models.FloatField()),
                ('bus3_lng', models.FloatField()),
                ('bus3_time', models.DateTimeField()),
                ('bus3_date', models.DateTimeField()),
                ('bus3_speed', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bus4_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus4_lat', models.FloatField()),
                ('bus4_lng', models.FloatField()),
                ('bus4_time', models.DateTimeField()),
                ('bus4_date', models.DateTimeField()),
                ('bus4_speed', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='LocationData',
        ),
    ]
