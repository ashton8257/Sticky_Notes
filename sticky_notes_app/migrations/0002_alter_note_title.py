# Generated by Django 5.0.6 on 2024-06-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sticky_notes_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]
