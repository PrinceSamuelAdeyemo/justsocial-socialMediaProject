# Generated by Django 4.1.1 on 2022-10-23 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_post_delete_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(upload_to='postImages'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 18, 37, 27, 746536)),
        ),
    ]
