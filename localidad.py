class Ubicacion:
    """
    Clase padre que almacena las coordenadas geograficas (latitud y longitud) de cualquier punto en el mapa.
    """

    def __init__(self, latitud, longitud):
        """
        Constructor que inicializa la latitud y longitud de la ubicacion.
        """
        self.latitud = latitud
        self.longitud = longitud

class Localidad(Ubicacion):
    """
    Clase hija que hereda de Ubicacion. Representa una zona especifica de Caracas guardando 
    su nombre y el municipio al que pertenece.
    """

    def __init__(self, municipio, localidad, latitud, longitud):
        """
        Constructor que inicializa el nombre y municipio de la zona, y utiliza la clase padre para guardar sus coordenadas.
        """
        super().__init__(latitud, longitud)
        self.municipio = municipio
        self.localidad = localidad

    def mostrar_datos(self): 
        """
        Imprime de forma ordenada en la consola los datos basicos de la localidad y sus coordenadas.
        """ 
        print("Municipio: " + self.municipio + " | Localidad: " + self.localidad + " | Latitud: " + str(self.latitud) + " | Longitud: " + str(self.longitud))