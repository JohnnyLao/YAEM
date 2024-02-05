# Generated by Django 4.2.2 on 2024-01-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_remove_dish_percentage_for_service"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="description",
            field=models.TextField(max_length=100, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="client",
            name="description_en",
            field=models.TextField(max_length=100, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="client",
            name="description_kk",
            field=models.TextField(max_length=100, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="client",
            name="description_ru",
            field=models.TextField(max_length=100, null=True, verbose_name="Описание"),
        ),
    ]