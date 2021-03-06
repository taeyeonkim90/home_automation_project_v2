# Generated by Django 2.0.2 on 2018-02-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.CharField(default='*', max_length=100)),
                ('hour', models.CharField(default='*', max_length=100)),
                ('day_of_week', models.CharField(default='*', max_length=100)),
                ('command', models.CharField(default='ls', max_length=100)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
