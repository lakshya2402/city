# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# connecting store and storedata so that the can connect with database
class store(models.Model):
    store_name= models.CharField(max_length=250, unique=True)
    # store_address= models.CharField(max_length=250)
    # store_contact_no= models.CharField(max_length=12)
    # store_lat =models.CharField(max_length=12)
    # store_lng =models.CharField(max_length=12)

    def __str__(self):
        return self.store_name

class storedata(models.Model):
    store_brand= models.ForeignKey(store, on_delete=models.CASCADE)
    store_city=models.CharField(max_length=250)
    def __str__(self):
        return self.store_city

class marchandise(models.Model):
    store_name=models.ForeignKey(store, on_delete=models.CASCADE)
    store_available=models.ForeignKey(storedata, on_delete=models.CASCADE)
    store_marchandise=models.CharField(max_length=250, unique=True)
    store_address= models.CharField(max_length=250)
    store_contact_no= models.CharField(max_length=12)
    store_lat =models.CharField(max_length=12)
    store_lng =models.CharField(max_length=12)
    def __str__(self):
        return str(self.store_marchandise)
