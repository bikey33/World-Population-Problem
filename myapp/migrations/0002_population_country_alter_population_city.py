# Generated by Django 4.0.6 on 2022-07-29 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='population',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.country'),
        ),
        migrations.AlterField(
            model_name='population',
            name='city',
            field=models.CharField(default=datetime.datetime(2022, 7, 29, 11, 20, 48, 188479, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]