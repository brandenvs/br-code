# Generated by Django 5.1.1 on 2024-10-16 12:41

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
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_id', models.IntegerField()),
                ('theme_id', models.IntegerField()),
                ('title', models.CharField(default='Untitled', max_length=35)),
                ('github_repository', models.CharField(default='Not available', max_length=255)),
                ('status', models.CharField(default='loading', max_length=35)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]