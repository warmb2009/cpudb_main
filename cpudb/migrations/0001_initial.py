# Generated by Django 2.2.2 on 2019-07-13 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('pic', models.CharField(default='', max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CodeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='cores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foundry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntegratedGraphics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Multiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MultiplierUnlocked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pageage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('transistors', models.CharField(default='', max_length=128, null=True)),
                ('die_size', models.CharField(default='', max_length=32, null=True)),
                ('t_case_max', models.CharField(default='', max_length=32, null=True)),
                ('frequency', models.CharField(default='', max_length=32, null=True)),
                ('turbo_clock', models.CharField(default='', max_length=32, null=True)),
                ('base_clock', models.CharField(default='', max_length=32, null=True)),
                ('voltage', models.CharField(default='', max_length=32, null=True)),
                ('released', models.CharField(default='', max_length=32, null=True)),
                ('part', models.CharField(default='', max_length=64, null=True)),
                ('smp_cpus', models.CharField(default='', max_length=32, null=True)),
                ('cache_l1', models.CharField(default='', max_length=32, null=True)),
                ('cache_l2', models.CharField(default='', max_length=32, null=True)),
                ('cache_l3', models.CharField(default='', max_length=32, null=True)),
                ('cache_l4', models.CharField(default='', max_length=32, null=True)),
                ('notes', models.TextField(default='', null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Brand')),
                ('codename', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.CodeName')),
                ('cores', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Core')),
                ('feature', models.ManyToManyField(to='cpudb.Feature')),
                ('foundry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='foundry_cpus', to='cpudb.Foundry')),
                ('generation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Generation')),
                ('integrated_graphics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.IntegratedGraphics')),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Market')),
                ('memory_support', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Memory')),
                ('multiplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Multiplier')),
                ('multiplier_unlocked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.MultiplierUnlocked')),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Pageage')),
                ('process_size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='process_size_cpus', to='cpudb.ProcessSize')),
                ('production_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.ProductionStatus')),
                ('socket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='socket_cpus', to='cpudb.Socket')),
                ('tdp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.TDP')),
                ('threads', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Thread')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu_Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('url', models.CharField(max_length=128, unique=True)),
                ('done', models.BooleanField(default=False)),
                ('cpu', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='cpudb.Cpus')),
            ],
        ),
    ]
