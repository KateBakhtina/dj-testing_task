# Generated by Django 5.0.2 on 2024-02-29 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_django_app', '0002_remove_quantity_groups'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['date_start']},
        ),
    ]
