# Generated by Django 3.2.5 on 2021-08-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_alter_team_team_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findmember',
            name='career',
            field=models.CharField(choices=[('1', '경력 무관'), ('2', '2년 미만'), ('3', '5년 미만'), ('4', '10년 미만'), ('5', '10년 이상')], max_length=1),
        ),
    ]