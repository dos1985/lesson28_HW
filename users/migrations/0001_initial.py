# Generated by Django 4.2 on 2023-05-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=8)),
                ("lng", models.DecimalField(decimal_places=6, max_digits=8)),
            ],
            options={
                "verbose_name": "Местположение",
                "verbose_name_plural": "Местположения",
            },
        ),
        migrations.CreateModel(
            name="UserRoles",
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
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                    "first_name",
                    models.CharField(max_length=50, null=True, verbose_name="Имя"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=100, null=True, verbose_name="Фамилия"),
                ),
                (
                    "username",
                    models.CharField(max_length=150, unique=True, verbose_name="Логин"),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Пароль"
                    ),
                ),
                ("age", models.PositiveIntegerField()),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("member", "Пользователь"),
                            ("moderator", "Модератор"),
                            ("admin", "Администратор"),
                        ],
                        default="member",
                        max_length=10,
                    ),
                ),
                ("location", models.ManyToManyField(to="users.location")),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
