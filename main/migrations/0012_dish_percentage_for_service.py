# Generated by Django 4.2.2 on 2024-01-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_alter_client_working_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="percentage_for_service",
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
