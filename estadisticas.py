import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Estadisticas:
    """
    Clase que funciona como motor matematico. Guarda el historial de consultas de la sesion 
    y calcula promedios, rankings y variabilidades.
    """

    def __init__(self):
        """
        Constructor que inicializa dos listas vacias en memoria para llevar el registro de las zonas consultadas y sus climas.
        """
        self.lista_clima = [] 
        self.lista_zonas = [] 

    def agregar_consulta(self, zona, clima):
        """
        Guarda el objeto de la zona y el objeto de su clima actual en las listas de la sesion activa.
        """
        self.lista_zonas.append(zona)
        self.lista_clima.append(clima)

    def mostrar_ranking(self, lista_zonas_memoria):
        """
        Recorre el historial de la sesion para calcular e imprimir la zona mas fria, la mas 
        caliente, el promedio general y agrupa los municipios con localidades sin coordenadas.
        """
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

        print("RANKINGS: ")    
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
            
            # Solo imprimimos el municipio si tiene zonas faltantes
            if len(faltantes_municipio) > 0:
                hay_faltantes = True
                print("-> " + mun.upper() + ":")
                for loc in faltantes_municipio:
                    print("- " + loc)
                    
        if hay_faltantes == False:
            print("Todas las zonas en memoria tienen coordenadas validas.")
        
        print("\n")
  
    def promedios_historicos(self, lista_dias, nombre_localidad):
        """
        Utiliza la libreria Pandas para calcular los records absolutos (calor, frio, lluvia, humedad) 
        de un periodo pasado y genera una tabla con los promedios desglosados por mes. Retorna dicha tabla.
        """
        print("\nANALISIS HISTORICO DE " + nombre_localidad.upper())
        if len(lista_dias) == 0:
            print("Error: Lista de dias vacia.")
            return None

        matriz_datos = []
            
        for dia in lista_dias: # Extraemos las 4 variables protegiendo contra nulos          
            temp = dia.temperatura if dia.temperatura != None else 0
            lluv = dia.lluvia if dia.lluvia != None else 0
            hum = dia.humedad if dia.humedad != None else 0
            vien = dia.viento if dia.viento != None else 0
            fila = [dia.fecha, temp, lluv, hum, vien]
            matriz_datos.append(fila)

        columnas = ["Fecha", "Temperatura", "Lluvia", "Humedad", "Viento"]
        tabla = pd.DataFrame(matriz_datos, columns=columnas)
        
        indice_calor = tabla["Temperatura"].idxmax()
        indice_frio = tabla["Temperatura"].idxmin()
        indice_lluvia = tabla["Lluvia"].idxmax()       
        indice_humedad = tabla["Humedad"].idxmax()
        
        año_calor = tabla["Fecha"][indice_calor][0:4]
        año_frio = tabla["Fecha"][indice_frio][0:4]
        año_lluvia = tabla["Fecha"][indice_lluvia][0:4]
        año_humedad = tabla["Fecha"][indice_humedad][0:4]
        
        print("\nRECORDS HISTORICOS DEL PERIODO")
        print("-> Año mas caluroso: " + año_calor + " (" + str(tabla["Temperatura"][indice_calor]) + " °C)")
        print("-> Año mas fresco: " + año_frio + " (" + str(tabla["Temperatura"][indice_frio]) + " °C)")
        print("-> Año con mayor lluvia: " + año_lluvia + " (" + str(tabla["Lluvia"][indice_lluvia]) + " mm)")
        print("-> Año con mayor humedad: " + año_humedad + " (" + str(tabla["Humedad"][indice_humedad]) + " %)")
        
        tabla["Mes"] = tabla["Fecha"].str.slice(0, 7)
        promedios_mes = tabla.groupby("Mes")[["Temperatura", "Lluvia", "Humedad", "Viento"]].mean()
        
        print("\nTABLA DE PROMEDIOS MENSUALES")
        pd.set_option('display.max_rows', None)
        print(promedios_mes.round(2))
        pd.reset_option('display.max_rows')
        
        matriz_clima = np.array(tabla[["Temperatura", "Lluvia", "Humedad", "Viento"]])
        promedios_generales = np.mean(matriz_clima, axis=0) 
        
        print("\nPROMEDIOS GENERALES DEL PERIODO")
        print("-> Temperatura promedio: " + str(round(promedios_generales[0], 2)) + " °C")
        print("-> Lluvia promedio: " + str(round(promedios_generales[1], 2)) + " mm")
        print("-> Humedad promedio: " + str(round(promedios_generales[2], 2)) + " %")
        print("-> Viento promedio: " + str(round(promedios_generales[3], 2)) + " km/h")
        
        return promedios_mes

    def graficar_historico(self, tabla_meses, nombre_localidad):
        """
        Utiliza la libreria Matplotlib para generar y mostrar dos ventanas visuales con subgraficos 
        que comparan la evolucion de las 4 variables climaticas a lo largo de los meses.
        """
        if tabla_meses is None:
            return

        meses = list(tabla_meses.index)
        temperaturas = list(tabla_meses["Temperatura"])
        lluvias = list(tabla_meses["Lluvia"])
        humedades = list(tabla_meses["Humedad"])
        vientos = list(tabla_meses["Viento"])

        cantidad_meses = len(meses)
        salto = cantidad_meses // 36
        if salto == 0:
            salto = 1

        posiciones = []
        etiquetas = []
        for i in range(0, cantidad_meses, salto):
            posiciones.append(i)
            etiquetas.append(meses[i])

        titulo_ventana_1 = "Temperatura y Lluvia de " + nombre_localidad
        plt.figure(num=titulo_ventana_1, figsize=(10, 8))

        plt.subplot(2, 1, 1)
        plt.plot(meses, temperaturas, color="red", marker="o")
        plt.title("Temperatura (°C)")
        plt.xticks(posiciones, etiquetas, rotation=45, fontsize=8)

        plt.subplot(2, 1, 2)
        plt.bar(meses, lluvias, color="blue")
        plt.title("Lluvia (mm)")
        plt.xticks(posiciones, etiquetas, rotation=45, fontsize=8)       
        plt.tight_layout() 

        titulo_ventana_2 = "Humedad y Viento de " + nombre_localidad
        plt.figure(num=titulo_ventana_2, figsize=(10, 8))

        plt.subplot(2, 1, 1)
        plt.plot(meses, humedades, color="green", marker="s")
        plt.title("Humedad Relativa (%)")
        plt.xticks(posiciones, etiquetas, rotation=45, fontsize=8)

        plt.subplot(2, 1, 2)
        plt.plot(meses, vientos, color="orange", marker="^")
        plt.title("Velocidad del Viento (km/h)")
        plt.xticks(posiciones, etiquetas, rotation=45, fontsize=8)
        plt.tight_layout() 

        plt.show()