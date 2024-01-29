# Generated by Django 4.2.2 on 2024-01-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_dish_popular_alter_dish_generated'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='spicy',
            field=models.BooleanField(default=0, verbose_name='Острое (знак)'),
        ),
        migrations.AddField(
            model_name='dish',
            name='vegetarian',
            field=models.BooleanField(default=0, verbose_name='Вегетерианское (знак)'),
        ),
    ]
