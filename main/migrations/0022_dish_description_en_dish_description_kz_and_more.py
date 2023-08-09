# Generated by Django 4.2.2 on 2023-08-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0021_client_address_en_client_address_kz_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="description_en",
            field=models.TextField(
                blank=True, max_length=100, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AddField(
            model_name="dish",
            name="description_kz",
            field=models.TextField(
                blank=True, max_length=100, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AddField(
            model_name="dish",
            name="description_ru",
            field=models.TextField(
                blank=True, max_length=100, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AddField(
            model_name="dish",
            name="name_en",
            field=models.CharField(max_length=30, null=True, verbose_name="Блюдо_RU"),
        ),
        migrations.AddField(
            model_name="dish",
            name="name_kz",
            field=models.CharField(max_length=30, null=True, verbose_name="Блюдо_RU"),
        ),
        migrations.AddField(
            model_name="dish",
            name="name_ru",
            field=models.CharField(max_length=30, null=True, verbose_name="Блюдо_RU"),
        ),
    ]
