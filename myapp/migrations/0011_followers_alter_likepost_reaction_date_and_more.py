# Generated by Django 4.1.1 on 2022-10-26 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_profile_posts_alter_likepost_reaction_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('follower', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='likepost',
            name='reaction_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 18, 19, 45, 589003)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 18, 19, 45, 584520)),
        ),
    ]
