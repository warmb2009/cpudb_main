# Generated by Django 2.2.2 on 2019-07-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpudb', '0008_auto_20190714_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpus',
            name='frequency',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
        migrations.RemoveField(
            model_name='cpus',
            name='memory_support',
        ),
        migrations.AddField(
            model_name='cpus',
            name='memory_support',
            field=models.ManyToManyField(blank=True, null=True, to='cpudb.Memory'),
        ),
    ]
