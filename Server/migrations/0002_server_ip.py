# Generated by Django 2.0.2 on 2019-05-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='ip',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]