# Generated by Django 4.2.11 on 2024-04-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("favorites", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="favorite",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
    ]
