from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('save/', views.save_data, name='save'),
]
