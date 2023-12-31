# Generated by Django 4.1.3 on 2023-11-18 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_b2p_flex_agents_program_program_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="b2p_reference",
            name="fte_capping",
            field=models.SmallIntegerField(
                blank=True,
                choices=[(1, "daily"), (2, "weekly"), (3, "monthly")],
                null=True,
            ),
        ),
    ]
