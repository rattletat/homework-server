# Generated by Django 3.0.5 on 2020-05-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20200512_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='first_error',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='first_failure',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='TestMessage',
        ),
    ]
