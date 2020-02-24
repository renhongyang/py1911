# Generated by Django 3.0.3 on 2020-02-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200218_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='question',
        ),
        migrations.AddField(
            model_name='user',
            name='questions',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]