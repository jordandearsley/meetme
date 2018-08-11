# Generated by Django 2.0.6 on 2018-07-26 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MeetMeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('slots', models.CharField(max_length=1000)),
                ('requests', models.CharField(max_length=255)),
                ('meetings', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_from', models.CharField(max_length=255)),
                ('user_to', models.CharField(max_length=255)),
                ('slot', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('status', models.NullBooleanField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_from', models.DateTimeField()),
                ('time_to', models.DateTimeField()),
                ('user', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('is_filled', models.BooleanField(default=False)),
                ('requests', models.CharField(max_length=255)),
            ],
        ),
    ]
