from django.shortcuts import render
from itertools import combinations

def calcular_combinacion_view(request):
    resultado = []
    errores = []

    if request.method == 'POST':
        try:
            min_calorias = int(request.POST.get('min_calorias'))
            max_peso = int(request.POST.get('max_peso'))

            if min_calorias < 0:
                errores.append("Las calorías mínimas no pueden ser negativas.")
            if max_peso < 0:
                errores.append("El peso máximo no puede ser negativo.")
        except (TypeError, ValueError):
            errores.append("Ingrese valores numéricos válidos para calorías mínimas y peso máximo.")
            return render(request, 'index.html', {'errores': errores})

        nombres = request.POST.getlist('nombre')
        pesos = request.POST.getlist('peso')
        calorias = request.POST.getlist('calorias')

        elementos = []
        for i, (n, p, c) in enumerate(zip(nombres, pesos, calorias), start=1):
            try:
                p = int(p)
                c = int(c)
                if p < 0 or c < 0:
                    errores.append(f"El peso y las calorías del producto {i} deben ser valores positivos.")
                else:
                    elementos.append({'nombre': n, 'peso': p, 'calorias': c})
            except (TypeError, ValueError):
                errores.append(f"Los valores de peso y calorías del producto {i} deben ser numéricos.")

        if not errores:
            resultado = obtener_mejor_combinacion(elementos, min_calorias, max_peso)

    return render(request, 'index.html', {'resultado': resultado, 'errores': errores})

def obtener_mejor_combinacion(elementos, min_calorias, max_peso):
    mejores = []
    menor_peso = float('inf')

    for r in range(1, len(elementos) + 1):
        for combo in combinations(elementos, r):
            total_peso = sum(e['peso'] for e in combo)
            total_cal = sum(e['calorias'] for e in combo)

            if total_cal >= min_calorias and total_peso <= max_peso:
                if total_peso < menor_peso:
                    mejores = list(combo)
                    menor_peso = total_peso

    return mejores
