from django.urls import path
from .views import calcular_combinacion_view

urlpatterns = [
    path('', calcular_combinacion_view, name='calcular_combinacion'),
    
]
