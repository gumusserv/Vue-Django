# Generated by Django 4.2.11 on 2024-05-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_alter_movie_discription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="discription",
            field=models.TextField(),
        ),
    ]