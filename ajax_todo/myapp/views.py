from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import generics

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Create your views here.
def list(request):
    return render(request, 'list.html')

