from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('hacked/',views.hacked,name="hacked"),
    path('karma/',views.karma,name="karma"),
    path('thor/',views.thor,name="thor"),
    path('covid/',views.covid,name="covid"),
]