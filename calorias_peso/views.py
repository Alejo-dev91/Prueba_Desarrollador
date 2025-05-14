from django.shortcuts import render
from itertools import combinations

def calcular_combinacion_view(request):
    resultado = []

    if request.method == 'POST':
        min_calorias = int(request.POST.get('min_calorias'))
        max_peso = int(request.POST.get('max_peso'))

        nombres = request.POST.getlist('nombre')
        pesos = request.POST.getlist('peso')
        calorias = request.POST.getlist('calorias')

        # Crea la lista de elementos con nombre, peso y calorías
        elementos = []
        for n, p, c in zip(nombres, pesos, calorias):
            elementos.append({
                'nombre': n,
                'peso': int(p),
                'calorias': int(c)
            })

        # Llamar la función que selecciona la mejor combinación
        resultado = obtener_mejor_combinacion(elementos, min_calorias, max_peso)

    return render(request, 'index.html', {'resultado': resultado})

def obtener_mejor_combinacion(elementos, min_calorias, max_peso):
    mejores = []
    menor_peso = float('inf')

    # Probar todas las combinaciones posibles
    for r in range(1, len(elementos) + 1):
        for combo in combinations(elementos, r):
            total_peso = sum(e['peso'] for e in combo)
            total_cal = sum(e['calorias'] for e in combo)

            # Verificamos si la combinación es válida
            if total_cal >= min_calorias and total_peso <= max_peso:
                if total_peso < menor_peso:
                    mejores = list(combo)
                    menor_peso = total_peso

    return mejores
