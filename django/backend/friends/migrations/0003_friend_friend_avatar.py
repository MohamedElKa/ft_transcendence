# Generated by Django 4.2.12 on 2024-05-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_alter_friend_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='friend_avatar',
            field=models.URLField(null=True),
        ),
    ]
