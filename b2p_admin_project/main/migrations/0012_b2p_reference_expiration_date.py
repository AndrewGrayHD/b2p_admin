# Generated by Django 4.2.7 on 2023-12-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_b2p_project_name_effectived_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='b2p_reference',
            name='expiration_date',
            field=models.DateField(default='2699-12-31'),
        ),
    ]
