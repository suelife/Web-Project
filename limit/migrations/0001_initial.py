# Generated by Django 2.1.1 on 2018-10-11 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('level', models.IntegerField()),
                ('index', models.IntegerField()),
                ('state', models.BooleanField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='limit.Menu')),
            ],
            options={
                'db_table': 'limit_menu',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=20, unique=True)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('state', models.BooleanField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'limit_role',
            },
        ),
        migrations.CreateModel(
            name='RoleMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('state', models.BooleanField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('menuid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='limit.Menu')),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='limit.Role')),
            ],
            options={
                'db_table': 'limit_rolemenu',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=20)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'limit_user',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='limit.Role')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='limit.User')),
            ],
            options={
                'db_table': 'limit_userrole',
            },
        ),
    ]