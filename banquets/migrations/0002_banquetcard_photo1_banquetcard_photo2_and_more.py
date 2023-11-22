# Generated by Django 4.2.2 on 2023-11-19 08:54

import banquets.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banquets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="banquetcard",
            name="photo1",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=banquets.models.banquet_logo_upload_to,
                verbose_name="Фото 1",
            ),
        ),
        migrations.AddField(
            model_name="banquetcard",
            name="photo2",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=banquets.models.banquet_logo_upload_to,
                verbose_name="Фото 2",
            ),
        ),
        migrations.AddField(
            model_name="banquetcard",
            name="photo3",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=banquets.models.banquet_logo_upload_to,
                verbose_name="Фото 3",
            ),
        ),
    ]