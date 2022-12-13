# Generated by Django 3.1.7 on 2022-12-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0014_attendance_status_resume'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='attendance',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='attendancefile',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
