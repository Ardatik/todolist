# Generated by Django 5.1.1 on 2024-10-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_list_model_prioritet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_model',
            name='prioritet',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
