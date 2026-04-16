from Interfaz.domain.Entidades.estudianteuser import Estudiante
from Interfaz.domain.Services.reglas import (
    ajustar_prediccion,
    interpretar_resultado
)
import numpy as np

def clasificar_estres(data, modelo, scaler):
    estudiante = Estudiante(data)

    entrada_sc = scaler.transform(estudiante.data)
    probabilidades = modelo.predict(entrada_sc, verbose=0)[0]

    clase_pred = ajustar_prediccion(probabilidades)

    resultado = interpretar_resultado(clase_pred, probabilidades)

    return resultado
