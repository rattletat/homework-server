# Generated by Django 3.0.5 on 2020-05-01 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200501_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='id_number',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]
