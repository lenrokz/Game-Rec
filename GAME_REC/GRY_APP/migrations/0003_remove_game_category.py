# Generated by Django 3.2 on 2021-11-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GRY_APP', '0002_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='category',
        ),
    ]