# Generated by Django 4.1.7 on 2023-04-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Preparation",
            fields=[
                ("preparation_id", models.AutoField(primary_key=True, serialize=False)),
                ("preparation_method_name", models.CharField(max_length=63)),
                ("preparation_method_description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Storage",
            fields=[
                ("storage_id", models.AutoField(primary_key=True, serialize=False)),
                ("storage_method_name", models.CharField(max_length=63)),
                ("storage_method_description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("product_url", models.CharField(max_length=63)),
                (
                    "category",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "Legumbres"),
                            (2, "Tubérculos"),
                            (3, "Raíces"),
                            (4, "Cereales"),
                            (5, "Frutas"),
                            (6, "Especies"),
                            (7, "Hortalizas"),
                            (8, "No convencionales"),
                        ]
                    ),
                ),
                ("scientific_name", models.CharField(max_length=63)),
                (
                    "scientific_name_variety",
                    models.CharField(blank=True, max_length=63, null=True),
                ),
                ("common_name", models.CharField(max_length=63)),
                (
                    "common_name_variety",
                    models.CharField(blank=True, max_length=63, null=True),
                ),
                (
                    "common_name_variety_alternate",
                    models.CharField(blank=True, max_length=63, null=True),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="images")),
                ("icon", models.ImageField(blank=True, null=True, upload_to="icons")),
                (
                    "center_origin",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "(I) Asia Oriental"),
                            (2, "(II) Subcontinente indio"),
                            (3, "(IIa) Archipiélago indo-malayo"),
                            (4, "(III) Asia Central"),
                            (5, "(IV) Asia Menor y Creciente Fértil"),
                            (6, "(V) Mediterráneo"),
                            (7, "(VI) Abisinia (actual Etiopía)"),
                            (8, "(VII) Mesoamérica"),
                            (9, "(VIII) Región andina tropical"),
                            (10, "(VIIIa) Región chilena"),
                            (11, "(VIIIb) Región brasileña-paraguaya"),
                            (12, "Sin clasificación"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "jan",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "feb",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "mar",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "apr",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "may",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "jun",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "jul",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "aug",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "sep",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "oct",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "nov",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "dec",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Sin disponibilidad"),
                            (1, "Poca disponibilidad"),
                            (2, "Buena disponibilidad"),
                            (3, "Temporada alta"),
                        ],
                        null=True,
                    ),
                ),
                ("nutrition_comment", models.TextField(blank=True, null=True)),
                ("preparation", models.ManyToManyField(to="products.preparation")),
                ("storage", models.ManyToManyField(to="products.storage")),
            ],
        ),
    ]
