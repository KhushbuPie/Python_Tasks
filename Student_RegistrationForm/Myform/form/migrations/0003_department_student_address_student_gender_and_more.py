# Generated by Django 5.0.6 on 2024-06-11 11:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0002_student_dob_student_mobile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="address",
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="hobbies",
            field=models.TextField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="pincode",
            field=models.CharField(max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="form.department"
            ),
            preserve_default=False,
        ),
    ]
