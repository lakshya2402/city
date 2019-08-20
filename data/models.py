# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# connecting store and storedata so that the can connect with database
class store(models.Model):
    store_name= models.CharField(max_length=250)
    store_address= models.CharField(max_length=250)
    store_contact_no= models.IntegerField(max_length=9)

class storedata(models.Model):
    store_location= models.ForeignKey(store, on_delete=models.CASCADE)
