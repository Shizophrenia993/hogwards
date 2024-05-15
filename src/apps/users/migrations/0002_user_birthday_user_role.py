# Generated by Django 5.0.4 on 2024-05-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='Гость', max_length=255),
        ),
    ]
