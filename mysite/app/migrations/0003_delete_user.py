# Generated by Django 4.2.11 on 2024-04-16 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
