from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'base.html')


def datalist(request):
    li = AjaxList.objects.all()
    context = {'li':list(li.values())}
    return JsonResponse(context)

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        new = AjaxList(title=title, body=body)
        new.save()
        return HttpResponse("New Data Add Success")
