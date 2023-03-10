# Generated by Django 3.2.16 on 2023-01-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_uom', models.CharField(max_length=50)),
                ('item_qty', models.FloatField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('updated_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='branch_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_uom', models.CharField(max_length=50)),
                ('item_qty', models.FloatField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('updated_by', models.CharField(max_length=200)),
            ],
        ),
    ]
