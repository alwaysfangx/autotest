# Generated by Django 2.1.5 on 2019-01-28 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appcase',
            old_name='creat_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='appcasestep',
            old_name='creat_time',
            new_name='create_time',
        ),
    ]
