# Generated by Django 2.1.1 on 2019-01-28 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('limit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='On_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IOtype', models.CharField(max_length=50)),
                ('money', models.IntegerField()),
                ('spendtype', models.CharField(max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('remark', models.CharField(max_length=500, null=True)),
                ('userid', models.ForeignKey(db_column='userid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='limit.User')),
            ],
            options={
                'db_table': 'on_account',
            },
        ),
    ]
