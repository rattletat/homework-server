# Generated by Django 3.0.5 on 2020-05-11 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import exercises.helper
import exercises.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0002_auto_20200511_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='exercise',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='exercises.Exercise'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(upload_to=exercises.helper.get_submission_path, validators=[exercises.validators.FileValidator(allowed_extensions=['py'], allowed_mimetypes=['text/x-python', 'text/plain'], max_size=4000, min_size=30)]),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testmessage',
            name='kind',
            field=models.CharField(choices=[('error', 'Error'), ('failure', 'Failure')], editable=False, max_length=8),
        ),
        migrations.AlterField(
            model_name='testmessage',
            name='message',
            field=models.TextField(default=None, editable=False),
        ),
        migrations.AlterField(
            model_name='testmessage',
            name='test',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='exercises.TestResult'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='job_id',
            field=models.CharField(editable=False, max_length=128),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='submission',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='exercises.Submission'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='success_count',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test_count',
            field=models.IntegerField(editable=False),
        ),
    ]
