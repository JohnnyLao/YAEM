# Generated by Django 4.2.2 on 2023-10-09 04:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_food_type2_options_remove_food_type2_client_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="food_type2",
            name="client",
            field=models.ManyToManyField(to="main.client", verbose_name="Клиент"),
        ),
    ]
