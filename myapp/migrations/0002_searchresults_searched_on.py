# Generated by Django 3.2 on 2021-05-11 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresults',
            name='searched_on',
            field=models.DateTimeField(null=True),
        ),
    ]