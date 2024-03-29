# Generated by Django 2.1.5 on 2020-05-16 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('score', models.IntegerField(max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Question')),
            ],
        ),
    ]
