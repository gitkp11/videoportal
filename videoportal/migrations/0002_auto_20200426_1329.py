# Generated by Django 3.0.2 on 2020-04-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='path',
        ),
        migrations.AddField(
            model_name='video',
            name='video_id',
            field=models.CharField(default='novideo', max_length=30),
            preserve_default=False,
        ),
    ]