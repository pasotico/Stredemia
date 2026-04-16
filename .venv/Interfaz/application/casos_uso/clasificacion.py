from domain.entities.estudiante import Estudiante
from domain.Services.reglas import (
    ajustar_prediccion,
    interpretar_resultado
)
def clasificar_estres(data, modelo, scaler):
    estudiante = Estudiante(data)

    entrada_sc = scaler.transform([estudiante.data])
    probabilidades = modelo.predict(entrada_sc, verbose=0)[0]

    clase_pred = ajustar_prediccion(probabilidades)

    resultado = interpretar_resultado(clase_pred, probabilidades)

    return resultado
