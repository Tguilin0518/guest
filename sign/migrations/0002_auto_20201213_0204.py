# Generated by Django 3.1.4 on 2020-12-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='creat_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='creat_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='real_name',
            new_name='realname',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default=12.948717948717949, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together={('phone', 'event')},
        ),
    ]
