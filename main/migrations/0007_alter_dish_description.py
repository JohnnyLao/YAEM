# Generated by Django 4.2.2 on 2023-06-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_dish_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.TextField(blank=True, max_length=80, verbose_name="Описание"),
        ),
    ]
