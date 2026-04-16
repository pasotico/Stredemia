def validar_formulario(
    valores_default,
    respuestas_sisco,
    min_cambios=10
):
    errores = []
    cambios = 0

    if any(r == "Nunca" for r in respuestas_sisco):
        errores.append("Debes responder todas las preguntas del cuestionario")


    return errores
