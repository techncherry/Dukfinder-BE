# Generated by Django 4.2.7 on 2023-11-22 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0005_remove_post_file_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hook_text',
        ),
    ]
