# Generated by Django 2.0.2 on 2019-05-30 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_auto_20190525_1430'),
        ('Server', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServerInert',
            new_name='ServerIntern',
        ),
    ]
