# Generated by Django 2.2 on 2020-06-23 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analysis', '0008_remove_analysis_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbased',
            name='user',
        ),
        migrations.RemoveField(
            model_name='perimeterbased',
            name='user',
        ),
        migrations.AddField(
            model_name='analysis',
            name='hotelBased',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analysis',
            name='perimeterBased',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analysis',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
