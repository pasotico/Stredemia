import numpy as np

def ajustar_prediccion(probabilidades):
    clase_pred = int(np.argmax(probabilidades))

    if probabilidades[2] >= 0.40:
        clase_pred = 2

    return clase_pred

def interpretar_resultado(clase_pred, probabilidades):
    etiquetas = {0: 'BAJO', 1: 'MEDIO', 2: 'ALTO'}
    colores   = {0: '🟢', 1: '🟡', 2: '🔴'}
    mensajes  = {
        0: "Tu nivel de estrés es bajo. ¡Sigue así! Mantén tus hábitos actuales.",
        1: "Tu nivel de estrés es moderado. Considera apoyo de Bienestar Universitario.",
        2: "Tu nivel de estrés es alto. ¡Busca apoyo de Bienestar Universitario pronto!."
    }

    return {
        "nivel": etiquetas[clase_pred],
        "color": colores[clase_pred],
        "mensaje": mensajes[clase_pred],
        "confianza": probabilidades[clase_pred],
        "probabilidades": probabilidades
    }
