# Generated by Django 5.0.2 on 2024-07-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_remove_notification_received'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='target_id',
            new_name='source_id',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
        migrations.AddField(
            model_name='notification',
            name='source_avatar',
            field=models.URLField(null=True),
        ),
    ]
