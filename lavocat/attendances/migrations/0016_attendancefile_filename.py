# Generated by Django 3.1.7 on 2023-01-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0015_auto_20221213_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancefile',
            name='filename',
            field=models.CharField(default='', max_length=124),
            preserve_default=False,
        ),
    ]