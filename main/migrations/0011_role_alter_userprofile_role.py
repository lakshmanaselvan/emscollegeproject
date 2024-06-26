# Generated by Django 5.0 on 2024-04-28 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.role'),
        ),
    ]
