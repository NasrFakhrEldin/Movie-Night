# Generated by Django 4.0.5 on 2022-09-11 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movienight'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieNightInvitaion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_confirmed', models.BooleanField(default=False)),
                ('is_attending', models.BooleanField(default=False)),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie_night', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='movies.movienight')),
            ],
            options={
                'unique_together': {('invitee', 'movie_night')},
            },
        ),
    ]
