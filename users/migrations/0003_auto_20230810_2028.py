# Generated by Django 3.1.4 on 2023-08-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230810_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzles_solved',
            name='puzzle_id',
            field=models.IntegerField(),
        ),
    ]
