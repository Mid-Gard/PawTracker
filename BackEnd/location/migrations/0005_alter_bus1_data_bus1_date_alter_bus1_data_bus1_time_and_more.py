# Generated by Django 4.1.7 on 2023-04-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("location", "0004_rename_bus2_location_bus1_data_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bus1_data",
            name="bus1_date",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="bus1_data",
            name="bus1_time",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="bus2_data",
            name="bus2_date",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="bus2_data",
            name="bus2_time",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="bus3_data",
            name="bus3_date",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="bus3_data",
            name="bus3_time",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="bus4_data",
            name="bus4_date",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="bus4_data",
            name="bus4_time",
            field=models.TextField(),
        ),
    ]
