# Generated by Django 3.0.5 on 2020-04-30 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200430_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='identifier',
        ),
    ]
