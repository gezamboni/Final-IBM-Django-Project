# Generated by Django 3.1.3 on 2023-02-06 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_question_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='ic_correct',
        ),
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='date_of_submission',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='time_of_submission',
            field=models.TimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
