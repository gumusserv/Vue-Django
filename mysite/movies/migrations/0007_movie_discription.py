# Generated by Django 4.2.11 on 2024-05-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0006_remove_movie_discription"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="discription",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]