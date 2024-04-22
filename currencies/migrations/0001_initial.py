# Generated by Django 5.0.4 on 2024-04-22 13:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
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
                (
                    "code",
                    models.CharField(
                        max_length=3,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="Currency code",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Currency name")),
                (
                    "symbol",
                    models.CharField(
                        blank=True,
                        null=True,
                        unique=True,
                        verbose_name="Currency symbol",
                    ),
                ),
            ],
        ),
    ]
