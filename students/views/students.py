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
