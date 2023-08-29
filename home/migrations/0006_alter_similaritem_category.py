# Generated by Django 4.2.4 on 2023-08-28 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_product_category_similaritem_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="similaritem",
            name="category",
            field=models.CharField(
                choices=[
                    ("outerwear", "Outerwear"),
                    ("top", "Top"),
                    ("bottom", "Bottom"),
                    ("shoes", "Shoes"),
                    ("accessory", "Accessory"),
                ],
                default="top",
                max_length=50,
            ),
        ),
    ]