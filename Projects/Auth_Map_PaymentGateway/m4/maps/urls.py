from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(r'',views.gmap_map, name="gmap"),
]