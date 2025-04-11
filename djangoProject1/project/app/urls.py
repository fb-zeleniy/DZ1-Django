from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('all/',index,name='all'),
    path('python/',index2,name='index2'),
    path('html/',index_html,name='index_html'),
    path('hw/', index3, name ='index3'),

]
