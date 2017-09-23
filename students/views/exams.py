#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Exam
import os, sys

#Views for Groups


def exams(request):
	exams = Exam.objects.all()
	return render(request, 'students/exams.html', {'exams':exams})

# Create your views here.
