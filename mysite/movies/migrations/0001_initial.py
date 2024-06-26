# Generated by Django 4.2.11 on 2024-04-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("movie_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("duration", models.IntegerField(help_text="Duration in minutes")),
                ("year", models.IntegerField()),
                ("director", models.CharField(max_length=255)),
                ("actors", models.TextField()),
                ("genre", models.CharField(max_length=100)),
                ("movie_link", models.URLField()),
                ("cover_image_url", models.URLField()),
                ("historical_rating", models.FloatField()),
            ],
        ),
    ]
