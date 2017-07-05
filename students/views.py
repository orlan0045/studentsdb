#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import os, sys

#Views for Students
def students_list(request):
	students = (
{
	'id':1,
  'first_name': u"Андрій",
  'last_name': u"Орлов",
	'ticket': 2,
	'image':'img/me.jpeg'	
},
{
	'id':2,
	'first_name': u'Максим',
	'last_name': u'Грибун',
	'ticket': 22,
	'image':'img/piv.png'
},
{
	'id':3,
	'first_name': u'Бомжик',
	'last_name': u'Непереможко',
	'ticket': 222,
	'image':'img/podoba3.jpg'
}
	)
	return render(request, 'students/students_list.html', {'students':students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)


#Views for Groups
def groups_list(request):
	groups = (
{
	'id':1,
  'name':u"ФЕІ-11",
  'leader': {'id': 1, 'name': u"Неалкогольний Джон"}
 },
{
	'id':2,
  'name':u"ФЕІ-12",
  'leader': {'id': 2, 'name': u"Істеричка Батьківна"}
},
{
	'id':3,
  'name':u"ФЕІ-13",
  'leader': {'id': 3, 'name': u"Рижулька Рижулівна"}
}
	)
	return render(request, 'students/groups_list.html', {'groups':groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' %gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group%s</h1>' %gid)				
# Create your views here.
