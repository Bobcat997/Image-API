# Generated by Django 4.1.7 on 2023-03-08 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_API', '0002_plan_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='link_expiration_time',
            field=models.IntegerField(default=300, validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(30000)]),
        ),
    ]
