import streamlit as st
import numpy as np

from Interfaz.infraestructure.modelo.cargar_modelo import cargar_modelo
from Interfaz.application.casos_uso.clasificacion import clasificar_estres
from Interfaz.desing.Mappings import *
from Interfaz.desing.constantes import opciones_sisco

st.set_page_config(page_title="STREDEMIA", page_icon="🧠")

modelo, scaler = cargar_modelo()

st.title("🧠 STREDEMIA")
st.markdown("**Clasificación no clínica del estrés académico**")
st.markdown("Universidad de Cundinamarca · Sede Fusagasugá")
st.divider()
st.markdown("❗Responde las preguntas con honestidad. "
            "\n⚠️ El resultado es orientativo y no reemplaza atención profesional.")
st.divider()

st.subheader("📋 Información general")

semestre = st.selectbox("Semestre actual", [
    '1 Semestre','2 Semestre','3 Semestre','4 Semestre',
    '5 Semestre','6 Semestre','7 Semestre','8 Semestre',
    '9 Semestre','10 Semestre'
])

edad = st.number_input("Edad (en años)", min_value=15, max_value=60, value=20)

estrato = st.selectbox("Estrato socioeconómico", [1, 2, 3, 4, 5, 6])

num_asignaturas = st.selectbox("Total de asignaturas matriculadas", [
    '1 a 3','4 a 6','7 a 9','Mayor o igual a 10'
])

promedio = st.selectbox("Promedio académico", [
    'Menor a 3.0','3.0 a 3.4','3.5 a 3.9','Mayor o igual a 4'
])

ha_perdido_cai = st.radio("¿Ha perdido CAI o CADIS?", ['Si', 'No'], horizontal=True)

horas_estudio = st.selectbox("Horas promedio de estudio diario", [
    'Menos de 1 hora','1-2 horas','2-3 horas','3-5 horas','6 o más horas'
])

trabaja = st.radio("¿Trabaja actualmente?", ['Si', 'No'], horizontal=True)

resp_familiar = st.radio(
    "¿Tienes responsabilidades familiares adicionales?",
    ['Si', 'No'], horizontal=True
)

horas_sueno = st.number_input(
    "En la última semana, ¿cuántas horas promedio ha dormido por noche?",
    min_value=1.0, max_value=12.0, value=6.0, step=0.5
)

calidad_sueno = st.selectbox("Calidad de sueño", [1, 2, 3, 4, 5],
    format_func=lambda x: {1:'Muy mala',2:'Mala',3:'Regular',4:'Buena',5:'Muy buena'}[x]
)

consume_cafeina = st.radio(
    "¿Consume frecuentemente cafeína o energizantes?",
    ['Si', 'No'], horizontal=True
)


st.subheader("⚡ Situaciones que te generan estrés")
st.caption("¿Con qué frecuencia las siguientes situaciones te preocupan o estresan?")

s1 = st.select_slider(
    "La sobrecarga de tareas y trabajos que tengo que realizar todos los días",
    options=opciones_sisco, value="Nunca")
s2 = st.select_slider(
    "La personalidad y el carácter de los/as profesores/as que me imparten clases",
    options=opciones_sisco, value="Nunca")
s3 = st.select_slider(
    "La forma de evaluación de mis profesores/as (ensayos, trabajos, búsquedas, etc.)",
    options=opciones_sisco, value="Nunca")
s4 = st.select_slider(
    "El nivel de exigencia de mis profesores/as",
    options=opciones_sisco, value="Nunca")
s5 = st.select_slider(
    "El tipo de trabajo que me piden los profesores (fichas, ensayos, mapas conceptuales, etc.)",
    options=opciones_sisco, value="Nunca")
s6 = st.select_slider(
    "Tener tiempo limitado para hacer el trabajo que me encargan los/as profesores/as",
    options=opciones_sisco, value="Nunca")
s7 = st.select_slider(
    "La poca claridad que tengo sobre lo que quieren los/as profesores/as",
    options=opciones_sisco, value="Nunca")
st.divider()
st.subheader("🌡️ Síntomas que has experimentado")
st.caption("¿Con qué frecuencia has tenido estos síntomas durante el semestre?")

s8  = st.select_slider("Fatiga crónica (cansancio permanente)", options=opciones_sisco, value="Nunca")
s9  = st.select_slider("Sentimientos de depresión y tristeza", options=opciones_sisco, value="Nunca")
s10 = st.select_slider("Ansiedad, angustia o desesperación",   options=opciones_sisco, value="Nunca")
s11 = st.select_slider("Problemas de concentración",           options=opciones_sisco, value="Nunca")
s12 = st.select_slider("Sentimiento de agresividad o irritabilidad", options=opciones_sisco, value="Nunca")
s13 = st.select_slider("Conflictos o tendencia a discutir",    options=opciones_sisco, value="Nunca")
s14 = st.select_slider("Desgano para realizar las labores escolares", options=opciones_sisco, value="Nunca")
st.divider()
st.subheader("🛡️ Estrategias que usas para manejar el estrés")
st.caption("¿Con qué frecuencia utilizas estas estrategias cuando algo te estresa?")

s15 = st.select_slider("Me concentro en resolver la situación que me preocupa", options=opciones_sisco, value="Nunca")
s16 = st.select_slider("Establezco soluciones concretas para resolver lo que me preocupa", options=opciones_sisco, value="Nunca")
s17 = st.select_slider("Analizo lo positivo y negativo de las soluciones posibles", options=opciones_sisco, value="Nunca")
s18 = st.select_slider("Mantengo el control sobre mis emociones para que no me afecte el estrés", options=opciones_sisco, value="Nunca")
s19 = st.select_slider("Recuerdo situaciones similares anteriores y cómo las resolví", options=opciones_sisco, value="Nunca")
s20 = st.select_slider("Elaboro un plan para enfrentar lo que me estresa y lo ejecuto", options=opciones_sisco, value="Nunca")
s21 = st.select_slider("Trato de obtener lo positivo de la situación que me preocupa", options=opciones_sisco, value="Nunca")

st.divider()

valores_default = {
    "semestre": "1 Semestre",
    "estrato": 1,
    "num_asignaturas": "1 a 3",
    "promedio": "Menor a 3.0",
    "ha_perdido_cai": "No",
    "horas_estudio": "Menos de 1 hora",
    "trabaja": "No",
    "resp_familiar": "No",
    "calidad_sueno": 3,
    "consume_cafeina": "No",
}


if st.button("🔍 Clasificar mi nivel de estrés", use_container_width=True):

    errores = []

    cambios = 0

    if semestre != valores_default["semestre"]: cambios += 1
    if estrato != valores_default["estrato"]: cambios += 1
    if num_asignaturas != valores_default["num_asignaturas"]: cambios += 1
    if promedio != valores_default["promedio"]: cambios += 1
    if ha_perdido_cai != valores_default["ha_perdido_cai"]: cambios += 1
    if horas_estudio != valores_default["horas_estudio"]: cambios += 1
    if trabaja != valores_default["trabaja"]: cambios += 1
    if resp_familiar != valores_default["resp_familiar"]: cambios += 1
    if calidad_sueno != valores_default["calidad_sueno"]: cambios += 1
    if consume_cafeina != valores_default["consume_cafeina"]: cambios += 1

    respuestas_sisco = [
        s1,s2,s3,s4,s5,s6,s7,
        s8,s9,s10,s11,s12,s13,s14,
        s15,s16,s17,s18,s19,s20,s21
    ]

    for r in respuestas_sisco:
        if r != "Nunca":
            cambios += 1

    if cambios < 28:
        st.error(f"⚠️ Debes responder todas las preguntas.")
        st.stop()


    entrada = np.array([[
        mapa_semestre[semestre],
        float(edad),
        float(estrato),
        mapa_asignaturas[num_asignaturas],
        mapa_promedio[promedio],
        mapa_sino[ha_perdido_cai],
        mapa_horas[horas_estudio],
        mapa_sino[trabaja],
        mapa_sino[resp_familiar],
        float(horas_sueno),
        float(calidad_sueno),
        mapa_sino[consume_cafeina],
        escala_sisco[s1], escala_sisco[s2], escala_sisco[s3],
        escala_sisco[s4], escala_sisco[s5], escala_sisco[s6],
        escala_sisco[s7], escala_sisco[s8], escala_sisco[s9],
        escala_sisco[s10], escala_sisco[s11], escala_sisco[s12],
        escala_sisco[s13], escala_sisco[s14], escala_sisco[s15],
        escala_sisco[s16], escala_sisco[s17], escala_sisco[s18],
        escala_sisco[s19], escala_sisco[s20], escala_sisco[s21],
    ]])

    resultado = clasificar_estres(entrada, modelo, scaler)

    st.divider()
    st.subheader("Resultado de la clasificación")

    col1, col2, col3 = st.columns(3)

    col1.metric("Nivel detectado", f"{resultado['color']} {resultado['nivel']}")
    col2.metric("Confianza", f"{resultado['confianza']*100:.1f}%")
    col3.metric("Clases evaluadas", "3")

    st.info(resultado['mensaje'])

    probs = resultado['probabilidades']

    st.markdown("**Probabilidades por nivel:**")
    st.progress(float(probs[0]), text=f"Bajo:  {probs[0]*100:.1f}%")
    st.progress(float(probs[1]), text=f"Medio: {probs[1]*100:.1f}%")
    st.progress(float(probs[2]), text=f"Alto:  {probs[2]*100:.1f}%")

    st.caption("⚠️ Este resultado es orientativo y no constituye un diagnóstico clínico.")
