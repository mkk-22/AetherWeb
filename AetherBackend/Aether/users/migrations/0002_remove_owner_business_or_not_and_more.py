# Generated by Django 5.1.5 on 2025-01-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='business_or_not',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='number_of_rooms',
        ),
        migrations.AddField(
            model_name='owner',
            name='plan_type',
            field=models.CharField(default='Home', max_length=8),
        ),
    ]
