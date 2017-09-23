#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
#from django.utils import six
#from collections import OrderedDict
from ..models import Student, Group
import os, sys


#Student Model
def students_list(request):
	students = Student.objects.all()

	order_by = request.GET.get('order_by', '')
	if order_by in ('id','last_name', 'first_name', 'ticket'):
			students = students.order_by(order_by)
			if request.GET.get('reverse', '') == '1':
				students = students.reverse()

 #paginate students
	paginator = Paginator(students, 3)
	page = request.GET.get('page')
	try:
  		students = paginator.page(page)
	except PageNotAnInteger:
	 	 #If page is not an integer, deliver first page.
	  	students = paginator.page(1)
	except EmptyPage:
	 	  # If page is out of range (e.g. 9999), deliver
		  # last page of results.
	  	students = paginator.page(paginator.num_pages)
	return render(request, 'students/students_list.html', {'students':students})

def students_add(request):
	if request.method == 'POST':
		if request.POST.get('add_button') is not None:
			errors={}
			data = {'middle_name' : request.POST.get('middle_name'), 'notes': request.POST.get('notes')}
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u'Ім*я є обов*язковим'
			else:
				data['first_name'] = first_name

			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u'Прізвище є обов*язковим'
			else:
				data['last_name'] = last_name

			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = u'Дата народження є обов*язковою'
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = u'Введіть коректний формат дати (напр. 1984-12-06)'
				else:
					data['birthday'] = birthday

			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = u'Номер білета є обов*язковим'
			else:
				data['ticket'] = ticket

			students_group = request.POST.get('students_group', '').strip()
			if not students_group:
				errors['students_group'] = u'Оберіть групу студента'
			else:
				groups = Group.objects.filter(pk=students_group)
				if len(groups) != 1:
					errors['students_group'] = u'Оберіть коректну групу студента'
				else:
					data['students_group'] = groups[0]

			photo = request.POST.get('photo', '').strip()
			if photo:
				data['photo'] = photo

			if not errors:
				student = Student(**data)
				student.save()
				return HttpResponseRedirect(u"%s?status_message=Студента %s успішно додано!"%(reverse('home'), student))
			else:
				return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title'), 'errors':errors})
		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано!'%reverse('home'))
	else:
		return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})
#def students_add(request):
#	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
