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

        print("RANKINGS")
        print("-> Zona mas caliente: " + zona_caliente + " (" + str(temp_max) + " °C)")
        print("-> Zona mas fria: " + zona_fria + " (" + str(temp_min) + " °C)")
        print("-> Temperatura promedio consultada: " + str(round(promedio, 2)) + " °C") 

        print("\nZONAS SIN COORDENADAS: ")
        municipios = []
        for zona in lista_zonas_memoria:
            if zona.municipio not in municipios:
                municipios.append(zona.municipio)
                            
        hay_faltantes = False
        for mun in municipios:
            faltantes_municipio = []
            for zona in lista_zonas_memoria:
                if zona.municipio == mun and (zona.latitud == None or zona.longitud == None):
                    faltantes_municipio.append(zona.localidad)

            if len(faltantes_municipio) > 0:
                hay_faltantes = True
                print("-> " + mun.upper() + ":")
                for loc in faltantes_municipio:
                    print("- " + loc)

        if hay_faltantes == False:
            print("Todas las zonas en memoria tienen coordenadas validas.")
                
        print("\n")

    def promedios_historicos(self, lista_dias, nombre_localidad):
          
        print("\nANALISIS HISTORICO DE " + nombre_localidad.upper())
        if len(lista_dias) == 0:
            print("Error: Lista de dias vacia.")
            return None

        matriz_datos = []

        for dia in lista_dias:  
            temp = dia.temperatura if dia.temperatura != None else 0
            lluv = dia.lluvia if dia.lluvia != None else 0
            hum = dia.humedad if dia.humedad != None else 0
            vien = dia.viento if dia.viento != None else 0
            fila = [dia.fecha, temp, lluv, hum, vien]
            matriz_datos.append(fila)
          