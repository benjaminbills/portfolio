# Generated by Django 3.2.4 on 2021-11-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20211126_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='techUsed',
            field=models.CharField(blank=True, default='Tech used', max_length=500),
        ),
    ]
