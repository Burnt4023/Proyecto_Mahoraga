from django.shortcuts import render
import requests

def buscador(request, nombre_carta):
    url = f"https://api.magicthegathering.io/v1/cards?name={nombre_carta}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        cartas = data.get('cards', [])

        # Diccionario para almacenar las cartas únicas según su nombre
        cartas_unicas = {}

        for carta in cartas:
            nombre = carta.get('name')
            if nombre not in cartas_unicas:
                cartas_unicas[nombre] = carta
            else:
                # Reemplazar la carta existente si la nueva carta es más reciente
                fecha_nueva = carta.get('releaseDate')
                fecha_existente = cartas_unicas[nombre].get('releaseDate')
                if fecha_nueva and (fecha_existente and fecha_nueva < fecha_existente):
                    cartas_unicas[nombre] = carta

        # Convertir el diccionario de cartas únicas de nuevo a una lista
        cartas_unicas = list(cartas_unicas.values())

        # Ordenar las cartas por fecha de lanzamiento en orden descendente
        cartas_unicas.sort(key=lambda x: x.get('releaseDate', ''), reverse=True)

        # Renderizar la plantilla buscador.html con las cartas únicas y el nombre de la carta buscada
        return render(request, 'buscador.html', {'cartas': cartas_unicas, 'nombre_carta': nombre_carta})
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error_message': str(e)})
def index(request):
    return render(request, 'index.html')