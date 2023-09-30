# Generated by Django 4.2.3 on 2023-09-27 00:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='current_week',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(models.IntegerField(default=1)), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term',
            name='length',
            field=models.IntegerField(default=1),
        ),
    ]
