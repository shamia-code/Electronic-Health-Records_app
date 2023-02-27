# Generated by Django 4.1.7 on 2023-02-26 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("patients", "0005_alter_patient_patient_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="registered_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patients_registered",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
