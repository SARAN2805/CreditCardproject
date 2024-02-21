# Generated by Django 4.1.2 on 2023-02-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_about_contact_assignlocker"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("fullname", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("mobile", models.CharField(blank=True, max_length=100, null=True)),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("father", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("pincode", models.CharField(blank=True, max_length=100, null=True)),
                ("regnumber", models.CharField(blank=True, max_length=100, null=True)),
                ("occup", models.CharField(blank=True, max_length=100, null=True)),
                ("income", models.CharField(blank=True, max_length=100, null=True)),
                ("image1", models.CharField(blank=True, max_length=100, null=True)),
                ("image2", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True, default="Not Updated Yet", max_length=200, null=True
                    ),
                ),
                ("creationdate", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Assignlocker",
        ),
        migrations.DeleteModel(
            name="Lockertype",
        ),
    ]