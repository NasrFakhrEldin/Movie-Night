# Generated by Django 4.0.5 on 2022-09-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.TextField(unique=True)),
                ('last_search', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('year', models.PositiveIntegerField()),
                ('runtime_minutes', models.PositiveIntegerField(null=True)),
                ('imdb_id', models.SlugField(unique=True)),
                ('plot', models.TextField(blank=True, null=True)),
                ('is_full_record', models.BooleanField(default=False)),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.genre')),
            ],
            options={
                'ordering': ['title', 'year'],
            },
        ),
    ]
