from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    form = StudentForm
    stu = Student.objects.all()
    context = {'form':form, 'stu':stu}
    return render(request, 'index.html', context)

@csrf_exempt
def save_data(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            s = Student(name=name, email=email, phone=phone)
            s.save()
            stu = Student.objects.values()
            stu_data = list(stu)
            return JsonResponse({'status':'success','stu_data':stu_data})
        else:
            return JsonResponse({'status':'error'})




