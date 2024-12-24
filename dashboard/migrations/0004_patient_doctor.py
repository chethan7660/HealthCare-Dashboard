# Generated by Django 5.1.3 on 2024-12-12 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_patient_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_patients', to='dashboard.doctor'),
        ),
    ]