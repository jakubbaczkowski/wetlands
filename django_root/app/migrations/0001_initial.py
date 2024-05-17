# Generated by Django 4.2.1 on 2023-05-04 17:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Publications",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("id_csv", models.IntegerField()),
                ("id_scopus", models.BigIntegerField()),
                ("id_wos", models.CharField(blank=True, max_length=255, null=True)),
                ("title", models.CharField(max_length=255)),
                ("abstract", models.TextField(blank=True, null=True)),
                ("doi", models.CharField(blank=True, max_length=255, null=True)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("url", models.URLField(blank=True, max_length=255, null=True)),
                ("pages", models.CharField(blank=True, max_length=255, null=True)),
                ("type", models.CharField(blank=True, max_length=255, null=True)),
                ("lang", models.CharField(blank=True, max_length=255, null=True)),
                ("volume", models.CharField(blank=True, max_length=255, null=True)),
                ("issue", models.CharField(blank=True, max_length=255, null=True)),
                ("issn", models.CharField(blank=True, max_length=255, null=True)),
                ("journal", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "disciplines",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("first_author_name", models.CharField(max_length=255)),
                (
                    "first_author_scopus_id",
                    models.BigIntegerField(blank=True, null=True),
                ),
                (
                    "first_author_affiliation_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "first_author_affiliation_country",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "co_authors",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                (
                    "keywords",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("citations_count", models.IntegerField(blank=True, null=True)),
                (
                    "references_crossref_id",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "references_scopus_id",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("citation_latest", models.TextField(blank=True, null=True)),
                (
                    "research_method",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("site_description", models.TextField(blank=True, null=True)),
                (
                    "spatial_scale",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("temporal_scale", models.IntegerField(blank=True, null=True)),
                ("ground_truth", models.BooleanField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("source", models.CharField(blank=True, max_length=255, null=True)),
                ("citation_count", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]