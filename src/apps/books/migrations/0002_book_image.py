# Generated by Django 5.0.4 on 2024-05-21 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='images.image'),
        ),
    ]
