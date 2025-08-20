from django.shortcuts import render, get_object_or_404
from .models import Practica

def home(request):
    practicas = Practica.objects.all()
    return render(request, 'practicas/home.html', {'practicas': practicas})

def practica_detalle(request, slug):
    practica = get_object_or_404(Practica, slug=slug)
    practicas = Practica.objects.all()  # 👈 aquí sacamos todas
    return render(request, 'practicas/detalle.html', {
        'practica': practica,
        'practicas': practicas,   # 👈 pasamos todas
    })
