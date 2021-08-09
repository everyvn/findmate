# Generated by Django 3.2.5 on 2021-08-09 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_member',
        ),
        migrations.AlterField(
            model_name='teamorg',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_org', to='teams.team'),
        ),
    ]
