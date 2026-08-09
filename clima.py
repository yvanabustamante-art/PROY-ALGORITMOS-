class Clima:
    """
    Clase que representa el estado del tiempo actual de una zona especifica en un momento dado.
    """
   
    def __init__(self, latitud, longitud, temperatura, humedad, viento, estado):
        """
        Constructor que recibe y guarda los datos puros extraidos de la API (temperatura, humedad, viento y codigo de estado).
        """
        self.latitud = latitud
        self.longitud = longitud
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.estado = estado

    def estado_tiempo(self):
        """
        Traduce el codigo numerico entregado por la API de Open-Meteo y devuelve un texto comprensible con la condicion climatica.
        Mapea exactamente los 28 codigos oficiales de la API Open-Meteo.
        """

        if self.estado == 0: return "Cielo despejado"
        elif self.estado == 1: return "Mayormente despejado"
        elif self.estado == 2: return "Parcialmente nublado"
        elif self.estado == 3: return "Nublado (Cubierto)"
        elif self.estado == 45: return "Niebla"
        elif self.estado == 48: return "Niebla con escarcha"
        elif self.estado == 51: return "Llovizna ligera"
        elif self.estado == 53: return "Llovizna moderada"
        elif self.estado == 55: return "Llovizna densa"
        elif self.estado == 56: return "Llovizna helada ligera"
        elif self.estado == 57: return "Llovizna helada densa"
        elif self.estado == 61: return "Lluvia ligera"
        elif self.estado == 63: return "Lluvia moderada"
        elif self.estado == 65: return "Lluvia fuerte"
        elif self.estado == 66: return "Lluvia helada ligera"
        elif self.estado == 67: return "Lluvia helada fuerte"
        elif self.estado == 71: return "Nieve ligera"
        elif self.estado == 73: return "Nieve moderada"
        elif self.estado == 75: return "Nieve fuerte"
        elif self.estado == 77: return "Granos de nieve"
        elif self.estado == 80: return "Chubascos ligeros"
        elif self.estado == 81: return "Chubascos moderados"
        elif self.estado == 82: return "Chubascos violentos"
        elif self.estado == 85: return "Chubascos de nieve ligeros"
        elif self.estado == 86: return "Chubascos de nieve fuertes"
        elif self.estado == 95: return "Tormenta electrica"
        elif self.estado == 96: return "Tormenta con granizo ligero"
        elif self.estado == 99: return "Tormenta con granizo fuerte"
        else: return "Desconocido (Codigo " + str(self.estado) + ")"

    def mostrar_clima(self):
        """
        Imprime en pantalla las variables climaticas actuales de forma estructurada para el usuario.
        """
        
        print("Temperatura: " + str(self.temperatura) + " °C")
        print("Humedad: " + str(self.humedad) + " %")
        print("Viento: " + str(self.viento) + " km/h")
        print("Estado: " + self.estado_tiempo())