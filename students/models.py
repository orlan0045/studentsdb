#!/usr/bin/python
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	"""Students Model"""

	class Meta(object):
		verbose_name=u'Студент'
		verbose_name_plural=u'Студенти'
	
	first_name = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u'Iм*я')

	last_name = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u'Прізвище')

	middle_name = models.CharField(
		max_length = 256,
		blank = True,
		verbose_name = u'По-батькові',
		default = '')

	birthday = models.DateField(
		blank = False,
		verbose_name = u'Дата народження',
		null = True)

	photo = models.ImageField(
		blank = True,
		verbose_name = u'Фото',
		null = True)

	ticket = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u'Білет')

	notes = models.TextField(
		blank = True,
		verbose_name = u'Додаткові нотатки')

	students_group = models.ForeignKey('Group',
		verbose_name = u'Група',
		blank = False,
		null = True,
		on_delete = models.PROTECT
		)

	def __unicode__(self):
		return u"%s %s"%(self.first_name,self.last_name)	




class Group(models.Model):
	"""Groups Model"""

	class Meta(object):
				verbose_name = u"Група"
				verbose_name_plural = u"Групи"	

	title = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва")

	leader = models.OneToOneField('Student',
		verbose_name=u"Староста",
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	notes = models.TextField(
		blank=True,
		verbose_name=u"Додаткові нотатки")

	def __unicode__(self):
		if self.leader:
			return u"%s" % (self.title,)
			#return u"%s (%s %s)" % (self.title, self.leader.first_name,	self.leader.last_name)
		else:
			return u"%s" % (self.title,)



class Journal(models.Model):
	"""Journals Model"""

	class Meta(object):
				verbose_name = u"Журнал"
				verbose_name_plural = u"Журнал"	


	journal_group = models.ForeignKey('Group',
		verbose_name = u'Група',
		blank = False,
		null = True,
		on_delete = models.PROTECT)

	def __unicode__(self):
		return u"%s"%(self.journal_group.title)



class Exam(models.Model):
	"""Exams Model"""

	class Meta(object):
				verbose_name = u"Екзамен"
				verbose_name_plural = u"Екзамени"

	exam_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва")

	# leader = models.OneToOneField('Student',
	# 	verbose_name=u"Староста",
	# 	blank=True,
	# 	null=True,
	# 	on_delete=models.SET_NULL)

	exam_date = models.DateField(
		blank = False,
		verbose_name = u'Дата екзамену',
		null = True)

	exam_group = models.ForeignKey('Group',
		verbose_name = u'Група',
		blank = False,
		null = True,
		on_delete = models.PROTECT)

	def __unicode__(self):
		return u"%s" % (self.exam_name,)
