# Generated by Django 3.2.4 on 2021-07-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]