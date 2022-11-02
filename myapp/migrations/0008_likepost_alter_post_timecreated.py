# Generated by Django 4.1.1 on 2022-10-24 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_post_postimage_alter_post_timecreated'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_username', models.CharField(max_length=100)),
                ('post_id', models.CharField(max_length=500)),
                ('reaction_username', models.CharField(max_length=100)),
                ('reaction_date', models.DateTimeField(default=datetime.datetime(2022, 10, 24, 4, 9, 33, 844355))),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 24, 4, 9, 33, 844355)),
        ),
    ]