# Generated by Django 5.0.6 on 2024-05-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tools",
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
                ("title", models.CharField(max_length=250)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("files", models.FileField(blank=True, upload_to="")),
                ("scripts", models.TextField(blank=True)),
                ("eternal_link", models.URLField()),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
