# Generated by Django 3.2.5 on 2021-07-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_auto_20210730_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('short_description', models.TextField(max_length=1024)),
                ('team_member', models.ManyToManyField(to='member.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]