# Generated by Django 2.2.4 on 2022-10-03 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete='cascade', related_name='comments', to='login_app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete='cascade', related_name='messages', to='login_app.User'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]