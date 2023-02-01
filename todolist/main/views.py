from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    tasks=Task.objects.all()
    return render(request,'main/index.html',{'title':'Главная','tasks':tasks})

def add(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form =TaskForm()
    context={
        'form':form
    }
    return render(request,'main/add.html',context)