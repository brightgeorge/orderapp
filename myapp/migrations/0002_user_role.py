# Generated by Django 3.2.16 on 2023-01-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
