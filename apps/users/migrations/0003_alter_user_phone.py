# Generated by Django 5.0.6 on 2024-06-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Телефон'),
        ),
    ]
