# Generated by Django 5.1.4 on 2025-01-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_varified',
            field=models.BooleanField(default=False),
        ),
    ]
