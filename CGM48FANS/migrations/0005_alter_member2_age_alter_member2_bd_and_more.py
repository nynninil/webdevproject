# Generated by Django 5.0.3 on 2024-09-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CGM48FANS', '0004_alter_songinformation_center_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member2',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='member2',
            name='bd',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member2',
            name='full_name_thai',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member2',
            name='nickname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member2',
            name='team',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
