# Generated by Django 5.0.1 on 2024-01-17 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalendarz', '0001_initial'),
        ('patient', '0001_initial'),
        ('worker', '0004_doctor_is_worker_secretary_is_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='worker.doctor'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]