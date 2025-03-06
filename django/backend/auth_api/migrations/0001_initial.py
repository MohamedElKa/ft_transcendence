# Generated by Django 4.2.16 on 2024-11-10 15:39

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=14, null=True, unique=True)),
                ('email', models.EmailField(max_length=128, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('avatar', models.URLField(default='https://github.com/shadcn.png')),
                ('status', models.CharField(default='Offline', max_length=20)),
                ('enable_2FA', models.BooleanField(default=False)),
                ('twofa_code', models.CharField(max_length=6, null=True)),
                ('passed_2FA', models.BooleanField(default=False, null=True)),
                ('oauth_42', models.BooleanField(default=False)),
                ('last_edit', models.DateTimeField(null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='grp', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='prm', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Scorex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('win_ratio', models.FloatField(default=0.0)),
                ('last_score', models.CharField(default='-', max_length=6)),
                ('level', models.FloatField(default=1.0)),
                ('required_xp', models.IntegerField(default=100)),
                ('current_xp', models.IntegerField(default=0)),
                ('total_xp', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
