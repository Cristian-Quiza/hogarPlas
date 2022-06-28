from django.shortcuts import render
from .froms import usersForm
 
# Create your views here.
# Solicitudes actuales que se pueden hacer dentro de estas vistas por archivo
# Definida para podificar y mostrar todo

def users_list(request):
    return render(request,"users/users_list.html")

def users_form(request):
    form = usersForm()
    return render(request,"users/users_form.html",{'form':form})

def users_delete(request):
    return

#def login(request):
 #   return