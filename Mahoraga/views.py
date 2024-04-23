from django.shortcuts import render

def buscador(request):
    return render(request, 'buscador.html')
def index(request):
    return render(request, 'index.html')