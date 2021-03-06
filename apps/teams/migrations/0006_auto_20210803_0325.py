# Generated by Django 3.2.5 on 2021-08-03 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20210802_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='purpose',
            field=models.CharField(blank=True, choices=[('1', '창업'), ('2', '취미'), ('3', '사이드프로젝트'), ('4', '스터디'), ('5', 'ETC')], max_length=1, null=True),
        ),
    ]
