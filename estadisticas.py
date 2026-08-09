import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Estadisticas:

    def __init__(self):
        self.lista_clima = []
        self.lista_zonas = []

    def agregar_consulta(self, zona, clima):