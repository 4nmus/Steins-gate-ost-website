# Generated by Django 4.2.5 on 2023-10-08 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Name of the song')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('song', models.FileField(upload_to='files')),
            ],
        ),
    ]
