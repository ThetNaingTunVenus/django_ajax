from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('datalist', views.datalist, name='datalist'),
    path('create', views.create, name='create'),
]