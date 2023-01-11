# Generated by Django 4.1.3 on 2022-12-05 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('table', '0002_remove_post_author_remove_post_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='height',
            field=models.PositiveSmallIntegerField(default=60, max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='width',
            field=models.PositiveSmallIntegerField(default=100, max_length=1),
        ),
    ]
