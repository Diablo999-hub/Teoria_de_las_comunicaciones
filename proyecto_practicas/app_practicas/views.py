from django.shortcuts import get_object_or_404, render

from .models import Practicas


# Create your views here.
def inicio(request):
    practicas = Practicas.objects.all()
    return render(request, "inicio.html", {"practicas": practicas})


def detalle(request, id):
    practica = get_object_or_404(Practicas, id=id)
    return render(request, "detalle.html", {"practica": practica})
