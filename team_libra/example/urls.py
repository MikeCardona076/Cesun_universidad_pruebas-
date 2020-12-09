from django.urls import path
from .class_views import *

app_name  = 'example'

urlpatterns = [
    #EJEMPLO DE URL 
    path('', Example.as_view(), name='Docente'),

    path('CREAR_USUARIO/', Crear_usuario.as_view(), name='example'),

    path('Materia/', Materias.as_view(), name='Materias'),

]

#     EJEMPLO MAS EXPLICADO .I.
#     path('NOMBRE DE LA URL QUE QUIERAS' , <---- NO OLVIDAR LAS COMAS 
#     NOMBRE DE LA CLASE QUE HICISTE.as_view() , 
#     name='NOMBRE PARA IDENTIFICAR ESTA URL EN ALGUNA FUNCION O CLASE')
