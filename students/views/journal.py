#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Journal
import os, sys

#Views for Groups


def journal(request):
	journal = Journal.objects.all()
	return render(request, 'students/journal.html', {'journal':journal})

# Create your views here.
