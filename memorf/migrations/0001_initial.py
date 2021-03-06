# Generated by Django 2.1.1 on 2018-10-11 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('limit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memorf',
            fields=[
                ('memoID', models.AutoField(primary_key=True, serialize=False)),
                ('memoTitle', models.CharField(max_length=40, null=True)),
                ('memoContent', models.CharField(blank=True, max_length=300, null=True)),
                ('memoState', models.CharField(max_length=1)),
                ('expiredate', models.DateField(null=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('lastUpgradeT', models.DateTimeField(auto_now=True)),
                ('cuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='limit.User', verbose_name='建立人員')),
            ],
            options={
                'db_table': 'memorf',
            },
        ),
    ]
