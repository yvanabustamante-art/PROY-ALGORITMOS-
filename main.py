import json # Usado solo para la lectura inicial del archivo con las zonas
from localidad import Localidad

def cargar_json(ruta_archivo):
    """
    Abre el archivo local de zonas, recorre el diccionario principal y transforma cada registro 
    valido en un objeto de la clase Localidad. Retorna la lista completa de objetos.
    """
    lista_zonas = []
    
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        datos_json = json.load(archivo)
        archivo.close()
        
        # Recorremos el diccionario 
        for municipio, lista_de_localidades in datos_json.items():
            # Recorremos cada localidad dentro de ese municipio
            for item in lista_de_localidades:
                nueva_zona = Localidad(
                    municipio,          
                    item["localidad"],  
                    item["latitud"],
                    item["longitud"]
                )
                lista_zonas.append(nueva_zona)
            
        return lista_zonas
        
    except FileNotFoundError:
        print("Error: No se encontro el archivo de datos.")
        return []
    except Exception as error_carga:
        print("Error inesperado al cargar datos: " + str(error_carga))
        return []
