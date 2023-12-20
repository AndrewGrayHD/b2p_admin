# Generated by Django 4.2.7 on 2023-12-07 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_b2p_flex_nesting_agents_program_assignment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='b2p_flex_nesting_agents_program',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.b2p_assignment'),
        ),
        migrations.AddField(
            model_name='b2p_flex_sme_ratio_program',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.b2p_assignment'),
        ),
        migrations.AddField(
            model_name='b2p_rates_program',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.b2p_assignment'),
        ),
    ]