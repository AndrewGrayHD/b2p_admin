# Generated by Django 4.2.7 on 2023-12-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_b2p_reference_expiration_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='b2p_flex_agents_program',
            new_name='b2p_flex_nesting_agents_program',
        ),
        migrations.AddField(
            model_name='b2p_project_name',
            name='expiration_date',
            field=models.DateField(default='2699-12-31'),
        ),
    ]