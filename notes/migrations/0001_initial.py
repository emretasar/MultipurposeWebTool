# Generated by Django 4.2.5 on 2023-09-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("title", models.CharField(max_length=100)),
                ("note", models.CharField(max_length=1000)),
                ("tag", models.CharField(max_length=20)),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("last_edit_date", models.DateTimeField()),
                ("owner", models.CharField(default="Not Known", max_length=16)),
            ],
        ),
    ]
