# Generated by Django 3.2.23 on 2024-01-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("test_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="testmodel",
            name="published",
            field=models.BooleanField(default=True),
        ),
    ]
