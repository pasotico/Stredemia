import pandas as pd

def transformar_in(datos: dict, scaler):
    transformar = pd.DataFrame([datos])
    transformar_escala = scaler.transform(transformar)
    return transformar_escala
