# Generated by Django 2.2.2 on 2019-06-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpudb', '0009_auto_20190629_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpus',
            name='generation',
            field=models.CharField(default='', max_length=64, null=True),
        ),
    ]