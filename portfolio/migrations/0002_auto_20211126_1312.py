# Generated by Django 3.2.4 on 2021-11-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='githublink',
            field=models.URLField(blank=True, default='Blank'),
        ),
        migrations.AddField(
            model_name='project',
            name='intro',
            field=models.CharField(blank=True, default='Blank', max_length=100),
        ),
    ]