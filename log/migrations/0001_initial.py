# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, help_text='', auto_created=True)),
                ('session', models.CharField(max_length=40, help_text='')),
                ('varname', models.CharField(max_length=30, db_index=True, help_text='')),
                ('stamp', models.DateTimeField(null=True, help_text='')),
                ('value', models.TextField(blank=True, help_text='')),
                ('user', models.ForeignKey(null=True, help_text='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, help_text='', auto_created=True)),
                ('session', models.CharField(max_length=40, help_text='')),
                ('url', models.CharField(max_length=500, help_text='')),
                ('stamp', models.DateTimeField(null=True, help_text='')),
                ('user', models.ForeignKey(help_text='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='requestlog',
            unique_together=set([('user', 'session', 'url', 'stamp')]),
        ),
        migrations.AlterUniqueTogether(
            name='log',
            unique_together=set([('user', 'session', 'varname', 'stamp')]),
        ),
    ]
