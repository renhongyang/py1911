# Generated by Django 3.0.3 on 2020-02-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0002_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='desc1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='图片描述1'),
        ),
        migrations.AlterField(
            model_name='recommend',
            name='desc2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='图片描述2'),
        ),
    ]
