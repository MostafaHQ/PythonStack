# Generated by Django 2.2.4 on 2022-10-01 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0007_auto_20221001_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(default='YYYY-MM-DD'),
            preserve_default=False,
        ),
    ]
