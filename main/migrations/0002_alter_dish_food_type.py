# Generated by Django 4.2.2 on 2023-06-12 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='food_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.food_type2', verbose_name='Подкатегория'),
        ),
    ]
