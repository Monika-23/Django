# Generated by Django 3.1.7 on 2021-04-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='fbimg',
            field=models.ImageField(upload_to='fimages/'),
        ),
    ]
