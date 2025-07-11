from django.contrib import admin
from django.urls import path
from website.views import *
urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('residential/',residential,name='residential'),
    path('industrial/',industrial,name='industrial'),
    path('commercial/',commercial,name='commercial'),
    path('DTCP_approved/',DTCP_approved ,name='DTCP_approved'),
    path('apartment/',apartment ,name='apartment'),
    path('renovation/',renovation ,name='renovation'),
]
