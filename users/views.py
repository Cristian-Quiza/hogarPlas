from django.shortcuts import render, redirect
from .froms import usersForm
from .models import Users
 
# Create your views here.
# Solicitudes actuales que se pueden hacer dentro de estas vistas por archivo
# Definida para podificar y mostrar todo

def users_list(request):
    context = {'users_list': Users.objects.all()}
    return render(request,"users/users_list.html", context)

def users_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = usersForm()
        else:
            users = Users.objects.get(pk = id)
            form = usersForm(instance = users)
        return render(request,"users/users_form.html",{'form':form})
    else:
        if id == 0:
            form = usersForm(request.POST)
        else:
            users = Users.objects.get(pk = id)
            form = usersForm(request.POST, instance = users)
        if form.is_valid():
            form.save()
        return redirect('/users/list')

def users_delete(request, id):
    users = Users.objects.get(pk = id)
    users.delete()    
    return redirect('/users/list')

#def login(request):
 #   return