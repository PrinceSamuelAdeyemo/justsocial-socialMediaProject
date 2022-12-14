# Generated by Django 4.1.1 on 2022-10-31 05:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_post_name_alter_likepost_reaction_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.post'),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='reaction_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 6, 12, 9, 565835)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 6, 12, 9, 565835)),
        ),
    ]
