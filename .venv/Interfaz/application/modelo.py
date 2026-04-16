import numpy as np
from Interfaz.infraestructure.cargar_modelo import cargar_modelo
from Interfaz.infraestructure.preprocesamiento import transformar_in

modelo, scaler = cargar_modelo()

def predecir_estres(datos: dict):
    X = transformar_in(datos, scaler)

    proba = modelo.predict(X)[0]

    umbral_alto = 0.40

    pred = np.argmax(proba)

    if proba[2] >= umbral_alto:
        pred = 2

    return pred, proba
