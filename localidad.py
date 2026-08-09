class Ubicacion: 

    def __init__(self, latitud, longitud): 
        self.latitud = latitud 
        self.longitud = longitud

class Localidad(Ubicacion):
    
    def __init__(self, municipio, localidad, latitud, longitud): 
        super().__init__(latitud, longitud) 
        self.municipio = municipio 
        self.localidad = localidad

    def mostrar_datos(self): 
        print("Municipio: " + self.municipio + " | Localidad: " + self.localidad + " | Latitud: " + str(self.latitud) + " | Longitud: " + str(self.longitud))