# Generated by Django 4.2.1 on 2023-05-09 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_rename_id_csv_publications_id_import"),
    ]

    operations = [
        migrations.RenameField(
            model_name="publications",
            old_name="id_wos",
            new_name="id_crossref",
        ),
    ]
