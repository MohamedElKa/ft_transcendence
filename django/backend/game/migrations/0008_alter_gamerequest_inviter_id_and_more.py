# Generated by Django 5.0.2 on 2024-06-02 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_gamerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerequest',
            name='inviter_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gamerequest',
            name='target_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
