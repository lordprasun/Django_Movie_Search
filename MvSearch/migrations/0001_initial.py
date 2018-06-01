# Generated by Django 2.0.3 on 2018-06-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imdb_score', models.FloatField()),
                ('popularity99', models.FloatField()),
                ('director', models.CharField(max_length=100)),
                ('genre', models.TextField()),
            ],
        ),
    ]
