# Generated by Django 4.1.3 on 2023-11-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_b2p_flex_sme_ratio_program_b2p_flex_agents_program"),
    ]

    operations = [
        migrations.AddField(
            model_name="b2p_flex_agents_program",
            name="assignment",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="b2p_flex_sme_ratio_program",
            name="assignment",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
