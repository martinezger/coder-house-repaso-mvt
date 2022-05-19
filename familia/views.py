from django.shortcuts import render
from django.http import HttpResponse
from familia.models import *

def hola_mundo(request):
    return HttpResponse("hola mundo")


def hola_soy_una_plantilla(request):
    german = Persona.objects.first()
    return HttpResponse(render(request, 'familia/index.html', {"about":german}))
