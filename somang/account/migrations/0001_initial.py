# Generated by Django 4.0.4 on 2022-04-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.TextField()),
                ('project_name', models.TextField()),
                ('description', models.TextField(null=True)),
                ('account_id', models.TextField()),
                ('account_pw', models.TextField()),
                ('profile_url', models.TextField(null=True)),
            ],
        ),
    ]
