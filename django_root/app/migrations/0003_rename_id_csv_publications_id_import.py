# Generated by Django 4.2.1 on 2023-05-09 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_publications_id_scopus"),
    ]

    operations = [
        migrations.RenameField(
            model_name="publications",
            old_name="id_csv",
            new_name="id_import",
        ),
    ]
