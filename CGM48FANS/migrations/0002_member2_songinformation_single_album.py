# Generated by Django 5.0.3 on 2024-09-26 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CGM48FANS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member2',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('team', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('nickname', models.CharField(max_length=100)),
                ('full_name_thai', models.CharField(max_length=200)),
                ('bd', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SongInformation',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_song', models.CharField(max_length=200)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CGM48FANS.member')),
                ('sembatsu', models.ManyToManyField(related_name='sembatsu_songs', to='CGM48FANS.member')),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_single', models.CharField(max_length=200)),
                ('copy', models.IntegerField()),
                ('list_songs', models.ManyToManyField(related_name='singles', to='CGM48FANS.songinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_album', models.CharField(max_length=200)),
                ('copy', models.IntegerField()),
                ('list_songs', models.ManyToManyField(related_name='albums', to='CGM48FANS.songinformation')),
            ],
        ),
    ]
