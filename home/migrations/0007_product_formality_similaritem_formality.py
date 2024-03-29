# Generated by Django 4.2.4 on 2023-08-29 00:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_similaritem_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="formality",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
        migrations.AddField(
            model_name="similaritem",
            name="formality",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]
