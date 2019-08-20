# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#this is add to get some request form server

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>this is the web page") 
