# Generated by Django 4.2.2 on 2023-08-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0014_city_name_en_city_name_kz_city_name_ru"),
    ]

    operations = [
        migrations.AddField(
            model_name="food_type2",
            name="name_en",
            field=models.CharField(
                max_length=30, null=True, verbose_name="Подкатегория"
            ),
        ),
        migrations.AddField(
            model_name="food_type2",
            name="name_kz",
            field=models.CharField(
                max_length=30, null=True, verbose_name="Подкатегория"
            ),
        ),
        migrations.AddField(
            model_name="food_type2",
            name="name_ru",
            field=models.CharField(
                max_length=30, null=True, verbose_name="Подкатегория"
            ),
        ),
    ]
