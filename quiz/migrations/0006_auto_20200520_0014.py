# Generated by Django 2.1.5 on 2020-05-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_score',
            field=models.IntegerField(choices=[(1, 'a1'), (5, 'a5'), (10, 'b10'), (50, 'b50'), (100, 'c100')], default=1),
        ),
    ]
