# LibrosBibliotecaApp/forms.py
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'ano_publicacion']

 # Agrega este método para personalizar el campo de autor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre del autor'})