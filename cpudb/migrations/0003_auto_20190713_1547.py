# Generated by Django 2.2.2 on 2019-07-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpudb', '0002_auto_20190713_1435'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pageage',
            new_name='Package',
        ),
        migrations.AlterField(
            model_name='cpus',
            name='brand',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='cpus',
            name='package',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
    ]
