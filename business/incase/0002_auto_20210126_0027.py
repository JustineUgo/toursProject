# Generated by Django 3.1.4 on 2021-01-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='email',
        ),
        migrations.AlterField(
            model_name='business',
            name='pic',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]
