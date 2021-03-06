# Generated by Django 3.2.5 on 2021-08-02 04:47

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='purpose',
            field=models.CharField(blank=True, choices=[('1', 'STARTUP'), ('2', 'HOBBY'), ('3', 'SIDE PROJECTS'), ('4', 'ETC')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='FindMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('msg', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('manpower', models.IntegerField()),
                ('career', models.CharField(choices=[('1', 'FRESHMAN'), ('2', '~2 YEARS'), ('3', '3~4 YEARS'), ('4', '5 YEARS~'), ('5', '10 YEARS~')], max_length=1)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
