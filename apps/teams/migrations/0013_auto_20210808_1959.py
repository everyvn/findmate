# Generated by Django 3.2.5 on 2021-08-08 10:59

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_team_team_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_member',
        ),
        migrations.AlterField(
            model_name='findmember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='find_member', to='teams.team'),
        ),
        migrations.CreateModel(
            name='TeamOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30, verbose_name='직책')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='teams.teamorg', verbose_name='parent')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='teams.team')),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
            },
        ),
    ]
