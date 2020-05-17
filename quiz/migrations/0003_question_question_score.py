# Generated by Django 2.1.5 on 2020-05-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200516_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_score',
            field=models.IntegerField(choices=[(1, 'Light'), (10, 'Medium'), (100, 'High')], default=1),
        ),
    ]
