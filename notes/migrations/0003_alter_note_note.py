# Generated by Django 4.1 on 2024-08-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0002_alter_note_last_edit_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="note",
            field=models.CharField(max_length=1600),
        ),
    ]
