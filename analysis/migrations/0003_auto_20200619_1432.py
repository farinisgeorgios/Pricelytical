# Generated by Django 2.2 on 2020-06-19 11:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20200619_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='plotdata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
