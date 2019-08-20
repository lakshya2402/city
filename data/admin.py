# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


# adding store values to admin pannel
from .models import store
# Register your models here.
admin.site.register(store)
