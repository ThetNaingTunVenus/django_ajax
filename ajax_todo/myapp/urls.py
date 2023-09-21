from django.urls import path
from . import views
urlpatterns = [
    path('list', views.list, name='list'),
    path('api/', views.TaskList.as_view(), name='TaskList'),
    path('api/<int:pk>/', views.TaskDetail.as_view(), name='TaskDetail'),
]
