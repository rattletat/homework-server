# Generated by Django 3.0.5 on 2020-05-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_exercise_relevant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='relevant',
            field=models.BooleanField(default=True, verbose_name='Fließt in die Wertung ein.'),
        ),
    ]
