# Generated by Django 2.1.5 on 2020-05-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20200516_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.IntegerField(),
        ),
    ]
