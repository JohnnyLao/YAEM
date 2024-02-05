# Generated by Django 4.2.2 on 2024-02-05 07:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("banquets", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="banquet",
            options={
                "ordering": ("id",),
                "verbose_name": "Банкетный зал",
                "verbose_name_plural": "Банкетные залы",
            },
        ),
        migrations.AlterModelOptions(
            name="banquetcard",
            options={
                "ordering": ("-z_index",),
                "verbose_name": "Карточку банкетного зала",
                "verbose_name_plural": "Карточки банкетных залов",
            },
        ),
    ]