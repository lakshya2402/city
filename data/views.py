# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render , HttpResponse
#this is for template function
from django.template import loader
#this is add to get some request form server
from django.http import HttpResponse, Http404
#to add store data
from .models import store, storedata, marchandise
from django.views.generic import TemplateView
#for login or register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
# Create your views here.

class storemap(TemplateView):
    template_name = 'storedetails.html'
def index(request):
    all_stores=store.objects.all()
    alllocation=marchandise.objects.all()
##ushing django.template
    # template=loader.get_template('index.html')
    # context={
    #     'all_stores':all_stores ,
    # }
    # return HttpResponse(template.render(context, request))
    context={
        'all_stores':all_stores ,
        'alllocation':alllocation,
    }
    return render(request,'index.html',context)

def store_details(request, store_id, marchandise_id):
    try:
        all_stores=store.objects.get(id=store_id)
        alllocation=marchandise.objects.get(id=marchandise_id)
    except store.DoesNotExist:
        raise Http404(request, '404.html',{'store':store})
    return HttpResponse("<h2>this is store no :" + str(store_id)  +"<h2>")

    # return HttpResponse("<h2>this is store no :" + str(store_id)  +"<h2>")
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
            return render(request = request,
                          template_name = "404.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "login_register.html",
                  context={"form":form})
