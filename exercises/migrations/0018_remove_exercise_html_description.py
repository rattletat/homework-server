# Generated by Django 3.0.5 on 2020-04-27 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0017_auto_20200427_0640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='html_description',
        ),
    ]