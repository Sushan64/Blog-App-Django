# Generated by Django 5.0.2 on 2025-02-16 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 16, 5, 47, 55, 26332, tzinfo=datetime.timezone.utc)),
        ),
    ]
