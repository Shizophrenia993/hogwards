# Generated by Django 5.0.4 on 2024-05-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0002_user_birthday_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='book_reservations',
            field=models.ManyToManyField(related_name='reservations', to='books.book'),
        ),
    ]
