#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import os, sys

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
