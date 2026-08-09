import requests
from clima import Clima
from dia import DiaHistorico

class Conexion:
    """
    Clase encargada de manejar todas las comunicaciones por internet (HTTP) con la API de Open-Meteo.
    """

    def __init__(self):
        """
        Constructor que define las direcciones web (URLs) base para consultar el clima actual y el clima historico.
        """
        self.url_base = "https://api.open-meteo.com/v1/forecast"
        self.url_historia = "https://archive-api.open-meteo.com/v1/archive"

    def consultar_actual(self, latitud, longitud):
        """
        Se conecta a la API utilizando las coordenadas recibidas, extrae los datos del clima 
        de ese momento y retorna un objeto de tipo Clima.
        """

        parametros = {
            "latitude": latitud,
            "longitude": longitud,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
        }

        try:
            respuesta = requests.get(self.url_base, params=parametros, timeout=10)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                temp = datos["current"]["temperature_2m"]
                hum = datos["current"]["relative_humidity_2m"]
                viento = datos["current"]["wind_speed_10m"]
                codigo = datos["current"]["weather_code"]
                objeto_clima = Clima(latitud, longitud, temp, hum, viento, codigo)
                return objeto_clima
            else:
                print("Error: La API devolvio el codigo " + str(respuesta.status_code))
                return None
        except requests.exceptions.RequestException as error_red:
            print("Error de conexion: " + str(error_red))
            return None

    def consultar_historico(self, latitud, longitud, fecha_inicio, fecha_fin):
        """
        Se conecta a la API de archivos pasados usando coordenadas y un rango de fechas. Extrae 
        las 4 variables diarias y retorna una lista llena de objetos DiaHistorico.
        """

        parametros = {
            "latitude": latitud,
            "longitude": longitud,
            "start_date": fecha_inicio,
            "end_date": fecha_fin,
            "daily": "temperature_2m_mean,precipitation_sum,relative_humidity_2m_mean,wind_speed_10m_max",
            "timezone": "auto"
        }
        
        try:
            respuesta = requests.get(self.url_historia, params=parametros, timeout=10)
            
            if respuesta.status_code == 200:
                datos = respuesta.json()
                lista_dias = []

                if "daily" not in datos:
                    print("Error: No se encontraron datos para estas fechas.")
                    return lista_dias
                    
                fechas = datos["daily"]["time"]
                temperaturas = datos["daily"]["temperature_2m_mean"]
                lluvias = datos["daily"]["precipitation_sum"]
                humedades = datos["daily"]["relative_humidity_2m_mean"]
                vientos = datos["daily"]["wind_speed_10m_max"]
                
                indice = 0
                while indice < len(fechas):
                    nuevo_dia = DiaHistorico(
                        fechas[indice], 
                        temperaturas[indice], 
                        lluvias[indice],
                        humedades[indice],
                        vientos[indice]
                    )
                    lista_dias.append(nuevo_dia)
                    indice = indice + 1
                    
                return lista_dias
                
            else:
                print("Error: La API devolvio codigo " + str(respuesta.status_code))
                return []
                
        except requests.exceptions.RequestException as error_red:
            print("Error de conexion: " + str(error_red))
            return []