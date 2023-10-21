# Generated by Django 3.1.4 on 2023-10-04 01:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_submission_delete_puzzles_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='attempts',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
    ]
