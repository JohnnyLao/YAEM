# Generated by Django 4.2.2 on 2024-01-29 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0014_alter_client_description_alter_client_description_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="generated",
            field=models.BooleanField(default=0, verbose_name="Сгенерировано"),
        ),
    ]