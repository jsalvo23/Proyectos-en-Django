# Libros/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.libro_list, name='libro_list'),
    path('libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libro/nuevo/', views.libro_nuevo, name='libro_nuevo'),
    path('libro/<int:pk>/editar/', views.editar_libro, name='editar_libro'),
    path('libro/<int:pk>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]
