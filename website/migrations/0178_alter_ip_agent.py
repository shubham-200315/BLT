# Generated by Django 5.1.4 on 2025-01-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0177_project_project_visit_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ip",
            name="agent",
            field=models.TextField(blank=True, null=True),
        ),
    ]