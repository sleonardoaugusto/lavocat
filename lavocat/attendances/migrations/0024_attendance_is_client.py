# Generated by Django 3.1.7 on 2024-03-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0023_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='is_client',
            field=models.BooleanField(default=False),
        ),
    ]
