# Generated by Django 4.1.3 on 2022-12-05 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_post_author_alter_post_height_alter_post_width'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
