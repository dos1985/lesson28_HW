# Generated by Django 4.2 on 2023-04-21 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_alter_categorymodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorymodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]