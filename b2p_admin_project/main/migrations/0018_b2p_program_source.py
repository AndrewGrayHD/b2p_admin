# Generated by Django 4.2.7 on 2023-12-19 22:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_b2p_flex_nesting_agents_program_assignment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='b2p_program_source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expiration_date', models.DateField(default='2699-12-31')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.b2p_site')),
                ('true_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.b2p_program')),
            ],
        ),
    ]
