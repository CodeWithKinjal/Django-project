import email
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#This Function will Add new Item and Show All items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['mobile']
            reg = User(name=nm, email=em, mobile=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'add/addandshow.html', {'form':fm, 'stu':stud})

#This Function will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi = User.objects.get(pk=id)
         fm = StudentRegistration(instance=pi)
    return render(request, 'add/update.html', {'form':fm})

#This Function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    