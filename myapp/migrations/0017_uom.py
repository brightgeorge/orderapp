# Generated by Django 3.2.16 on 2023-01-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='uom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom_name', models.CharField(max_length=200)),
                ('uom_created_by', models.CharField(max_length=200)),
                ('uom_flag', models.CharField(max_length=2)),
            ],
        ),
    ]
