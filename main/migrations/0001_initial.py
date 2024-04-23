# Generated by Django 5.0 on 2024-04-22 16:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('token', models.CharField(default=None, max_length=100)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('student', 'student'), ('staff', 'staff')], max_length=200)),
                ('designation', models.CharField(blank=True, choices=[('AP', 'AP'), ('Event Management', 'Event Management')], max_length=20, null=True)),
                ('has_module_perms', models.BooleanField(default=False)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]