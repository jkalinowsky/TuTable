# Generated by Django 4.2.5 on 2023-09-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]