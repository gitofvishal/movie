from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('download/<int:id>',views.download),
    path('search',views.search),
    path('apiread',views.apiread),
    path('apireadone/<int:id>',views.apireadone),
    path('apisearch/<str:name>',views.readsearch),
]
