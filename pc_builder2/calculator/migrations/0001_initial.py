# Generated by Django 5.1.1 on 2024-09-12 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseCPU",
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
                ("name", models.CharField(max_length=100)),
                ("perfomance_index", models.FloatField()),
                ("socket", models.IntegerField()),
                ("is_graphics", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="BaseGPU",
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
                    "short_name",
                    models.CharField(
                        max_length=100, verbose_name="Сокращенное название"
                    ),
                ),
                ("perfomance_index", models.FloatField()),
                ("tdp", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="BaseMotherBoard",
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
                ("name", models.CharField(max_length=100)),
                ("cost", models.FloatField()),
                ("socket", models.IntegerField()),
                ("power_phases", models.IntegerField()),
                ("type_of_memory", models.CharField(max_length=100)),
                ("chipset", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="BasePowerUnit",
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
                ("name", models.CharField(max_length=100)),
                ("power", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="BaseRAM",
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
                ("name", models.CharField(max_length=100)),
                ("value_gb", models.IntegerField()),
                ("type", models.CharField(max_length=100)),
                ("frequency", models.IntegerField(null=True)),
                ("is_game", models.BooleanField()),
                ("count", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                ("cpu", models.FloatField()),
                ("gpu", models.FloatField()),
                ("motherboard", models.FloatField()),
                ("ram", models.FloatField()),
                ("power_unit", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Configuration",
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
                    "cpu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="calculator.basecpu",
                    ),
                ),
                (
                    "gpu",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="calculator.basegpu",
                    ),
                ),
                (
                    "motherboard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="calculator.basemotherboard",
                    ),
                ),
                (
                    "power_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="calculator.basepowerunit",
                    ),
                ),
                (
                    "ram",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="calculator.baseram",
                    ),
                ),
            ],
        ),
    ]