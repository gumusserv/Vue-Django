# Generated by Django 4.2.11 on 2024-04-21 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("favorites", "0002_favorite_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="favorite",
            name="comment",
        ),
    ]
