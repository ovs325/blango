# Generated by Django 3.2.5 on 2022-03-29 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_i'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='i',
        ),
    ]
