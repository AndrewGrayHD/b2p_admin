# Generated by Django 4.2.7 on 2023-11-24 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_b2p_reference_fte_capping'),
    ]

    operations = [
        migrations.AddField(
            model_name='b2p_project_name',
            name='effectived_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]