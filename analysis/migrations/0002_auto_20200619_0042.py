# Generated by Django 2.2 on 2020-06-18 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='context',
            new_name='content',
        ),
    ]
