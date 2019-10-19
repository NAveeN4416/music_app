# Generated by Django 2.0.6 on 2019-10-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20191018_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.FileField(default='image.png', upload_to='industries/artists/albums/<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.FileField(default='image.png', upload_to='industries/artists/<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='industry',
            name='image',
            field=models.FileField(default='image.png', upload_to='industries'),
        ),
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(default='image.png', upload_to='industries/artists/albums/tracks/<django.db.models.fields.CharField>'),
        ),
    ]
