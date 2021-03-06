# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_auto_20150503_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 8, 16, 39, 469000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 8, 16, 39, 469000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 8, 16, 39, 469000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 8, 16, 39, 469000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 8, 16, 39, 469000)),
            preserve_default=True,
        ),
    ]
