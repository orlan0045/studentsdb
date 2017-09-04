# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_students_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430')),
            ],
            options={
                'verbose_name': '\u0416\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u0416\u0443\u0440\u043d\u0430\u043b',
            },
        ),
    ]