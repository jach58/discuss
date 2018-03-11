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
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('submitted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
