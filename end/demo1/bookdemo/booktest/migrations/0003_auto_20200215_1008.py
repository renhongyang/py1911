# Generated by Django 3.0.3 on 2020-02-15 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20200211_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='rhy', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.CharField(blank=True, db_column='description', max_length=50, null=True),
        ),
    ]
