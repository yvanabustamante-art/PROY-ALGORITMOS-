import json 
from localidad import Localidad

def cargar_json(ruta_archivo):
    
    lista_zonas = []
    
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        datos_json = json.load(archivo)
        archivo.close()
        
        
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
def reporte_inicial(lista_zonas):
    print("\nREPORTE INICIAL DE ZONAS DE CARACAS\n")
    
    if len(lista_zonas) == 0:
        print("La lista de zonas esta vacia.")
    else:
        for zona in lista_zonas:
            zona.mostrar_datos()           
    print("\n")

if __name__ == "__main__":
    lista_memoria = cargar_json("zonas.json")
    reporte_inicial(lista_memoria) 

    if len(lista_memoria) > 0:
        from conexion import Conexion
        from buscador import Buscador
        from estadisticas import Estadisticas
        
        api = Conexion()
        motor = Buscador()
        datos_sesion = Estadisticas()
        
        datos_sesion.revisar_coordenadas(lista_memoria)
        
        salir = False
        while salir == False: 
            print("\nMENU PRINCIPAL METEOCARACAS: ")
            print("1. Busqueda jerarquica (Municipio/Localidad)")
            print("2. Busqueda directa (Nombre)")
            print("3. Ranking de la sesion (Frio/Caliente)")
            print("4. Busqueda historica por fechas (Promedios)")
            print("5. Salir")
            
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1" or opcion == "2":
                zona_resultado = None
                
                if opcion == "1":
                    zona_resultado = motor.buscar_jerarquia(lista_memoria)
                elif opcion == "2":
                    zona_resultado = motor.buscar_directo(lista_memoria)
                    
                if zona_resultado != None:
                    print("\nPANEL DEL CLIMA: ")
                    zona_resultado.mostrar_datos()
                    
                    clima_actual = api.consultar_actual(zona_resultado.latitud, zona_resultado.longitud)
                    
                    if clima_actual != None:
                        clima_actual.mostrar_clima()
                        datos_sesion.agregar_consulta(zona_resultado, clima_actual)
                    
            elif opcion == "3":
                datos_sesion.mostrar_ranking()
                
            elif opcion == "4":
                zona_historia = motor.buscar_directo(lista_memoria)
                
                if zona_historia != None:
                    print("Nota: Las fechas deben tener el formato AAAA-MM-DD")
                    fecha_ini = input("Ingrese la fecha de inicio: ")
                    fecha_fin = input("Ingrese la fecha de fin: ")
                    
                    print("Consultando el archivo meteorologico...")
                    datos_pasados = api.consultar_historico(
                        zona_historia.latitud, 
                        zona_historia.longitud, 
                        fecha_ini, 
                        fecha_fin
                    )
                    
                    if len(datos_pasados) > 0:                       
                        tabla_mensual = datos_sesion.promedios_historicos(datos_pasados, zona_historia.localidad) 
                        
                        abrir = input("\nDesea abrir grafico comparativo [S/n]: ")
                        
                        if abrir == "S" or abrir == "s" or abrir == "":
                            print("Abriendo grafico comparativo...")
                            print("Cierre la ventana del grafico para continuar.")
                            datos_sesion.graficar_historico(tabla_mensual, zona_historia.localidad)
                        elif abrir == "N" or abrir == "n":
                            print("Grafico omitido.")
                        else:
                            print("Error: Opcion no valida. Grafico omitido.")
                        
            elif opcion == "5":
                print("Saliendo...\n")
                salir = True
                
            else:
                print("Error: Opcion no valida.")