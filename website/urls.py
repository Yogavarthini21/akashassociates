from django.contrib import admin
from django.urls import path
from website.views import *
urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('residential/',residential,name='residential'),
]
