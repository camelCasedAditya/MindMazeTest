# Generated by Django 4.2.3 on 2023-11-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("puzzles", "0010_alter_puzzle_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="puzzle",
            name="explination",
            field=models.TextField(default="Insert Explination"),
        ),
    ]
