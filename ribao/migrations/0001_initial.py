# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raw_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'pending'), (b'1', b'published')])),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'unpulblished'), (b'1', b'published')])),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='daily',
            field=models.ForeignKey(blank=True, to='ribao.Daily', null=True),
        ),
    ]
