# Generated by Django 5.1 on 2024-09-24 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_remove_useroffer_is_a_child_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='sport_name',
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.location', verbose_name='Lieu'),
        ),
    ]
