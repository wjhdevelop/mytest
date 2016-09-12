# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OaUser',
            fields=[
                ('oa_user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('oa_username', models.CharField(max_length=50, verbose_name=b'OA\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('passwd', models.CharField(max_length=50, verbose_name=b'OA\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
            ],
            options={
                'verbose_name': 'OA\u7528\u6237\u914d\u7f6e',
                'verbose_name_plural': 'OA\u7528\u6237\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='SisServe',
            fields=[
                ('serv_id', models.CharField(max_length=20, serialize=False, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8ID', primary_key=True)),
                ('serv_ip', models.GenericIPAddressField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8IP')),
                ('serv_port', models.IntegerField(default=8081, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\xab\xaf\xe5\x8f\xa3')),
                ('serv_name', models.CharField(max_length=30, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pub_key', models.CharField(max_length=32, verbose_name=b'Sisense\xe5\x85\xac\xe9\x92\xa5')),
                ('description', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'verbose_name': 'Sisense\u670d\u52a1\u5668\u914d\u7f6e',
                'verbose_name_plural': 'Sisense\u670d\u52a1\u5668\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='SisUserAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sis_username', models.EmailField(max_length=254, verbose_name=b'Sisense\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d/\xe9\x82\xae\xe7\xae\xb1')),
                ('oa_user_id', models.CharField(max_length=50, verbose_name=b'OA\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('is_save_cookie', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbf\x9d\xe5\xad\x98cookie')),
                ('is_default', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe9\xbb\x98\xe8\xae\xa4\xe7\x99\xbb\xe5\xbd\x95\xe5\xb9\xb3\xe5\x8f\xb0')),
                ('serv_id', models.ForeignKey(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8ID', to='blog.SisServe')),
            ],
            options={
                'verbose_name': 'Sisense\u7528\u6237\u914d\u7f6e',
                'verbose_name_plural': 'Sisense\u7528\u6237\u914d\u7f6e',
            },
        ),
    ]
