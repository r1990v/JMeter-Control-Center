# Generated by Django 2.2 on 2021-04-29 13:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analyzer', '0001_initial'),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JMeterTestPlanParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'jmeter_parameter',
            },
        ),
        migrations.CreateModel(
            name='LoadGenerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(default='', max_length=200, unique=True)),
                ('num_cpu', models.CharField(default='', max_length=200)),
                ('memory', models.CharField(default='', max_length=200)),
                ('memory_free', models.CharField(default='', max_length=200)),
                ('la_1', models.CharField(default='', max_length=200)),
                ('la_5', models.CharField(default='', max_length=200)),
                ('la_15', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='', max_length=200)),
                ('reason', models.CharField(default='', max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'load_generator',
            },
        ),
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(default=0)),
                ('pid', models.IntegerField(default=0)),
                ('destination', models.CharField(default='https://dest', max_length=200)),
                ('destination_port', models.IntegerField(default=443)),
                ('delay', models.FloatField()),
                ('started', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'proxy',
            },
        ),
        migrations.CreateModel(
            name='ScriptParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'script_parameter',
            },
        ),
        migrations.CreateModel(
            name='TestRunning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_file_dest', models.CharField(default='', max_length=200)),
                ('monitoring_file_dest', models.CharField(default='', max_length=200)),
                ('testplan_file_dest', models.CharField(default='', max_length=200)),
                ('log_file_dest', models.CharField(default='', max_length=200)),
                ('display_name', models.CharField(default='', max_length=100)),
                ('start_time', models.BigIntegerField()),
                ('pid', models.IntegerField(default=0)),
                ('jmeter_remote_instances', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('workspace', models.CharField(default='', max_length=200)),
                ('is_running', models.BooleanField(default=False)),
                ('build_number', models.IntegerField(default=0)),
                ('rampup', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('result_start_line', models.IntegerField(default=0)),
                ('result_file_size', models.IntegerField(default=0)),
                ('locked', models.BooleanField(default=False)),
                ('build_path', models.CharField(default='', max_length=600)),
                ('last_analyzed', models.DateTimeField(default=None, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzer.Project')),
            ],
            options={
                'db_table': 'test_running',
            },
        ),
        migrations.CreateModel(
            name='TestRunningData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('test_running', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controller.TestRunning')),
            ],
            options={
                'db_table': 'test_running_data',
            },
        ),
        migrations.CreateModel(
            name='LoadGeneratorServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=200)),
                ('ssh_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.SSHKey')),
            ],
            options={
                'db_table': 'load_generator_server',
            },
        ),
        migrations.CreateModel(
            name='JmeterInstanceStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzer.Project')),
            ],
            options={
                'db_table': 'jmeter_instance_statistic',
            },
        ),
        migrations.CreateModel(
            name='JmeterInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0)),
                ('port', models.IntegerField(default=0)),
                ('jmeter_dir', models.CharField(default='', max_length=300)),
                ('threads_number', models.IntegerField(default=0)),
                ('java_args', models.CharField(default='', max_length=1000)),
                ('load_generator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controller.LoadGenerator')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzer.Project')),
                ('test_running', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controller.TestRunning')),
            ],
            options={
                'db_table': 'jmeter_instance',
            },
        ),
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(default='', max_length=1000)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('load_generator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controller.LoadGenerator')),
            ],
            options={
                'db_table': 'activity_log',
            },
        ),
        migrations.CreateModel(
            name='ProjectGraphiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('value', models.CharField(default='', max_length=10000)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzer.Project')),
            ],
            options={
                'db_table': 'project_graphite_settings',
                'unique_together': {('project', 'value')},
            },
        ),
    ]
