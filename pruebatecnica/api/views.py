from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor
from .forms import AutorForm

def index(request):
    return HttpResponse("Bienvenido a la app de Libros")

def autor_detail(request, autor_id):
    autor = Autor.objects.get(id = autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor.nombre = form.cleaned_data['nombre']
            autor.save()
    else:
        form = AutorForm(instance=autor)
    context = {'autor':autor, 'form': form}

    return render(request, 'api/autor_detail.html',context)
