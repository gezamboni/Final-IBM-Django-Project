# Generated by Django 3.1.3 on 2023-02-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20230206_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=1.0),
        ),
    ]
