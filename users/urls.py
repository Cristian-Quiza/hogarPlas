from django.urls import path, include
from . import views

urlpatterns = [

    # Patrones URL hay que especificar las direcciones url el punto de registro de la app 
    # Patrones url dentro se pueden apreciar las asignaciones de url para adimin 
    # Para barra diagonal - Formulario
    
    # Rutas de Actualizacion
    path('', views.users_form, name='users_insert'), # solicitudes de obtencion y publicacion para la operacion de insercion
    path('<int:id>/', views.users_form, name='users_update'), # solicitudes de obtencion y publicacion para la operacion de actualizacion
    path('delete/<int:id>/', views.users_delete, name='users_delete'),
    path('list/', views.users_list, name='users_list') # solicitudes de obtencion y mostrar todos los registros 
]