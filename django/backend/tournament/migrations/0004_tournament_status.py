# Generated by Django 5.0.2 on 2024-08-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_tournament_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='status',
            field=models.CharField(default='WG', max_length=10),
        ),
    ]
