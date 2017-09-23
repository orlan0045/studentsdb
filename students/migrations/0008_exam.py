# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_remove_journal_group_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('exam_date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0443')),
                ('exam_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430')),
            ],
            options={
                'verbose_name': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d',
                'verbose_name_plural': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d\u0438',
            },
        ),
    ]
