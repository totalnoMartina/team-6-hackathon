# Generated by Django 3.1.13 on 2022-01-29 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]
