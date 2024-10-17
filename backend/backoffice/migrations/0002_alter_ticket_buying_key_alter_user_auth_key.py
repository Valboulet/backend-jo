# Generated by Django 5.1.2 on 2024-10-11 19:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='buying_key',
            field=models.UUIDField(default=uuid.uuid4, verbose_name="Clé d'achat"),
        ),
        migrations.AlterField(
            model_name='user',
            name='auth_key',
            field=models.UUIDField(default=uuid.uuid4, verbose_name="Clé d'authentification"),
        ),
    ]
