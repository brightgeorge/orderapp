# Generated by Django 3.2.16 on 2023-01-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='flag',
            new_name='item_flag',
        ),
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]