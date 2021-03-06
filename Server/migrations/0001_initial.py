# Generated by Django 2.0.2 on 2019-05-30 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Service', '0002_auto_20190525_1430'),
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.CharField(max_length=30)),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ServerClient',
            fields=[
                ('server_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Server.Server')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
            ],
            bases=('Server.server',),
        ),
        migrations.CreateModel(
            name='ServerInert',
            fields=[
                ('server_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Server.Server')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Service.Section')),
            ],
            bases=('Server.server',),
        ),
        migrations.AddField(
            model_name='app',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Server'),
        ),
    ]
