# Generated by Django 4.1.3 on 2022-12-05 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_table_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='author',
        ),
    ]
