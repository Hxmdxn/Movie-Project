# Generated by Django 5.0.3 on 2024-07-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_cards_detailed_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cards",
            name="detailed_description",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
