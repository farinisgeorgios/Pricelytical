# Generated by Django 2.2 on 2020-06-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0007_auto_20200623_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='user',
        ),
    ]
