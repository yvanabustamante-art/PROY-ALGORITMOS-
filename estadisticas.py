import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Estadisticas:

    def __init__(self):
        self.lista_clima = []
        self.lista_zonas = []

    def agregar_consulta(self, zona, clima): 
        self.lista_zonas.append(zona)
        self.lista_clima.append(clima)
        
    def mostrar_ranking(self, lista_zonas_memoria):
        print("\nESTADISTICAS DE LA SESION ")
        
        if len(self.lista_clima) == 0:
            print("Error: No hay consultas registradas en esta sesion.")
            return
            
        temp_max = self.lista_clima[0].temperatura
        temp_min = self.lista_clima[0].temperatura
        zona_caliente = self.lista_zonas[0].municipio + " - " + self.lista_zonas[0].localidad
        zona_fria = self.lista_zonas[0].municipio + " - " + self.lista_zonas[0].localidad

        suma_temperaturas = 0
        contador = 0

        while contador < len(self.lista_clima):
            clima_actual = self.lista_clima[contador]
            zona_actual = self.lista_zonas[contador]

            suma_temperaturas = suma_temperaturas + clima_actual.temperatura
            
            if clima_actual.temperatura > temp_max:
                temp_max = clima_actual.temperatura
                zona_caliente = zona_actual.municipio + " - " + zona_actual.localidad
                
            if clima_actual.temperatura < temp_min:
                temp_min = clima_actual.temperatura
                zona_fria = zona_actual.municipio + " - " + zona_actual.localidad
                
            contador = contador + 1

        promedio = suma_temperaturas / len(self.lista_clima)   