# Generated by Django 4.1.7 on 2023-03-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='size',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
