class DiaHistorico:
    """
    Clase que sirve como molde para representar y guardar los datos meteorologicos de un dia especifico en el pasado.
    """

    def __init__(self, fecha, temperatura, lluvia, humedad, viento):
        """
        Constructor que inicializa un nuevo dia historico con su fecha, temperatura, lluvia, humedad y viento.
        """
        self.fecha = fecha
        self.temperatura = temperatura
        self.lluvia = lluvia
        self.humedad = humedad
        self.viento = viento