# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , HttpResponse
#this is add to get some request form server

from django.http import HttpResponse
# Create your views here.

def index(request):
        mydic={'this_is_index':"hey i am index using django"}
        return render(request, 'index.html', context=mydic)
