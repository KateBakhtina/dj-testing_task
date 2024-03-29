# Generated by Django 5.0.2 on 2024-03-01 22:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_django_app', '0004_studygroup'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_groups', to='my_django_app.product'),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
