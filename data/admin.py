# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import store,storedata,marchandise




# adding store values to admin pannel

# Register your models here.
admin.site.register(store)
admin.site.register(storedata)
admin.site.register(marchandise)
