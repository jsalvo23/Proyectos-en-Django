# LibrosBibliotecaApp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libro_list.html', {'libros': libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'detalle_libro.html', {'libro': libro})

def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('detalle_libro', pk=libro.pk)
    else:
        form = LibroForm()
    return render(request, 'editar_libro.html', {'form': form, 'nuevo': True})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save()
            return redirect('detalle_libro', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form, 'nuevo': False})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        libro.delete()
        return redirect('libro_list')
    return render(request, 'eliminar_libro.html', {'libro': libro})
