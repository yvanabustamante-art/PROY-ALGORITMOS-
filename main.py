import json # Usado solo para la lectura inicial del archivo con las zonas
from localidad import Localidad

# Lee el archivo JSON local y convierte cada registro en un objeto Localidad.
def cargar_json(ruta_archivo):
    lista_zonas = []
    
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        datos_json = json.load(archivo)
        archivo.close()
        
        # Transformar los diccionarios del JSON en objetos de la clase Localidad
        for item in datos_json:
            nueva_zona = Localidad(
                item["municipio"],
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
