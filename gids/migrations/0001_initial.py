# Generated by Django 2.2.5 on 2019-09-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('channel', models.IntegerField(default=1)),
                ('start_date', models.DateTimeField(verbose_name='start_date')),
                ('end_date', models.DateTimeField(verbose_name='end_date')),
                ('channel_type', models.CharField(choices=[('radio', 'Radio'), ('television', 'Television')], max_length=20, unique=True)),
            ],
        ),
    ]
