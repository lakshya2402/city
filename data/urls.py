from django.conf.urls import url
from . import views
from .views import storemap


urlpatterns=[
    #this is our home page
    url(r'^$', views.index , name='index'),
    #this is our data base connected storedata
    url(r'storedetails/', storemap.as_view(), name='storemap'),
    url(r'^(?P<store_id>[0-9]+)/$', views.store_details, name='store_details'),
    url(r'register_form/',views.register,name="register")

]
