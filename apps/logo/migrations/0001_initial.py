# Generated by Django 5.0.6 on 2024-06-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Logo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=250)),
                ("subtitle", models.CharField(blank=True, max_length=250)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/img/logo/"
                    ),
                ),
            ],
        ),
    ]
