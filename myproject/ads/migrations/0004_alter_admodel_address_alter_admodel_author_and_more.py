# Generated by Django 4.2 on 2023-04-21 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_alter_categorymodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admodel",
            name="address",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="admodel",
            name="author",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="admodel",
            name="description",
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="admodel",
            name="is_published",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="admodel",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="categorymodel",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]