# Generated by Django 5.0.2 on 2024-02-13 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_industry_state_job_job_type_job_industry_job_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='city',
        ),
    ]