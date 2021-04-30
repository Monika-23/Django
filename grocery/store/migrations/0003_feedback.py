# Generated by Django 3.1.7 on 2021-04-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210425_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbname', models.CharField(max_length=200)),
                ('fbemail', models.EmailField(max_length=200)),
                ('fbdesc', models.TextField()),
                ('fbimg', models.FileField(upload_to='fimages/')),
                ('fbtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]