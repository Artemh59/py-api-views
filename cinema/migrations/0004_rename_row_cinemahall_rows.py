# Generated by Django 4.1 on 2023-12-07 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_movie_actors_alter_movie_genres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='row',
            new_name='rows',
        ),
    ]