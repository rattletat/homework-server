# Generated by Django 3.0.5 on 2020-04-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200430_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.UUIDField(default=None),
        ),
    ]
