# Generated by Django 2.2 on 2020-06-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='hotel_id',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
