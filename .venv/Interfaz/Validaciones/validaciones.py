def validar_formulario(
    valores_usuario,
    valores_default,
    respuestas_sisco,
    min_cambios=28
):
    errores = []
    cambios = 0

    for key in valores_default:
        if valores_usuario[key] != valores_default[key]:
            cambios += 1

    for r in respuestas_sisco:
        if r != "Nunca":
            cambios += 1

    if cambios < min_cambios:
        errores.append(f"Debes completar todo el formulario.")

    return errores
