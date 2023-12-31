# Generated by Django 4.1.3 on 2023-11-17 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_b2p_flex_agents_program_assignment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="b2p_flex_agents_program",
            name="program",
            field=models.CharField(
                blank=True, db_index=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="b2p_flex_agents_program",
            name="lob",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="b2p_flex_sme_ratio_program",
            name="lob",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name="b2p_rates_program",
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
                (
                    "program",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                ("lob", models.CharField(blank=True, max_length=255, null=True)),
                ("site", models.CharField(blank=True, max_length=255, null=True)),
                ("assignment", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "true_program",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main.b2p_program",
                    ),
                ),
                (
                    "true_site",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main.b2p_site",
                    ),
                ),
            ],
        ),
    ]
