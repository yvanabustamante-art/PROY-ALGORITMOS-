class Buscador:
    """
    Clase encargada de agrupar las herramientas para filtrar y buscar localidades especificas dentro de la lista en memoria.
    """

    def buscar_jerarquia(self, lista_zonas):
        """
        Muestra los municipios disponibles, solicita al usuario elegir uno y luego le permite 
        seleccionar una localidad especifica que tenga coordenadas validas. Retorna el objeto encontrado.
        """
        print("\nBUSQUEDA JERARQUICA ")
        municipios = []

        for zona in lista_zonas:
            if zona.municipio not in municipios:
                municipios.append(zona.municipio)

        print("Municipios disponibles:")
        for mun in municipios:
            print("- " + mun)

        elegido = input("Escriba el nombre del municipio: ")

        localidades_validas = []
        for zona in lista_zonas:
            if zona.municipio.lower() in elegido.lower() and zona.latitud != None and zona.longitud != None:
                localidades_validas.append(zona)

        if len(localidades_validas) == 0:
            print("Error: Municipio no encontrado o sin localidades con coordenadas validas.")
            return None

        print("\nLocalidades disponibles en " + elegido.upper() + ":")
        for loc in localidades_validas:
            print("- " + loc.localidad)

        loc_elegida = input("Escriba el nombre de la localidad: ")

        for zona in localidades_validas:
            if zona.localidad.lower() in loc_elegida.lower():
                return zona

        print("Error: Localidad no encontrada en la lista mostrada.")
        return None

    def buscar_directo(self, lista_zonas):
        """
        Busca localidades basandose en una palabra o fragmento de texto ingresado por el usuario. 
        Muestra las coincidencias validas y permite elegir una. Retorna el objeto seleccionado.
        """

        print("\nBUSQUEDA DIRECTA ")
        texto = input("Escriba el nombre de la localidad: ")

        coincidencias = []
        for zona in lista_zonas:
            if texto.lower() in zona.localidad.lower() and zona.latitud != None and zona.longitud != None:
                coincidencias.append(zona)

        if len(coincidencias) == 0:
            print("Error: No se encontraron localidades validas con esa palabra.")
            return None

        print("\nCoincidencias encontradas:")
        contador = 1
        for loc in coincidencias:
            print(str(contador) + ". " + loc.localidad + " (Municipio " + loc.municipio + ")")
            contador = contador + 1

        seleccion = input("Seleccione el numero: ")
        
        if seleccion.isdigit():
            indice = int(seleccion) - 1 
            if indice >= 0 and indice < len(coincidencias):
                return coincidencias[indice]
                
        print("Error: Seleccion no valida.")
        return None