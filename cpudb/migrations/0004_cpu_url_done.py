# Generated by Django 2.2.2 on 2019-06-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpudb', '0003_cpu_url_cpu'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu_url',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]