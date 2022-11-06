from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('download/<int:id>',views.download),
    path('search',views.search),
    path('gerne/<str:gerne>',views.gerne),
    path('searchyear/<str:y>',views.searchyear),
    path('searchgerne/<str:gerne>',views.searchgerne),
    path('release_year/<str:y>',views.release_year),
    path('apiread',views.apiread),
    path('apireadone/<int:id>',views.apireadone),
    path('apisearch/<str:name>',views.readsearch),
]
