# Generated by Django 3.0.5 on 2020-05-22 05:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0016_auto_20200522_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='number',
            field=models.PositiveSmallIntegerField(default=None, editable=False, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]