# Generated by Django 5.0.3 on 2024-09-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CGM48FANS', '0002_member2_songinformation_single_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songinformation',
            name='sembatsu',
            field=models.ManyToManyField(related_name='sembatsu_songs', to='CGM48FANS.member2'),
        ),
    ]
