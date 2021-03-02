# Generated by Django 3.1.4 on 2021-01-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20210126_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='endorsement',
            name='endorses',
            field=models.ManyToManyField(related_name='endorses', to='business.Business'),
        ),
        migrations.AddField(
            model_name='media',
            name='played',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='endorsement',
            name='endorsers',
            field=models.ManyToManyField(related_name='endorsers', to='business.Business'),
        ),
        migrations.AlterField(
            model_name='shelf',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shelfphoto',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
