# Generated by Django 4.1.3 on 2022-12-06 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0009_table_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='number',
        ),
    ]
