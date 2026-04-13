import pandas as pd
import numpy as np
xlsx =  pd.read_excel('../datos/raw/TEST_ ESTRÉS ACADÉMICO(1-322).xlsx')
sí_filter = next(c for c in xlsx.columns if 'Durante el transcurso ' in c)

nm = xlsx[xlsx[sí_filter] == 'SI'].reset_index(drop=True)
nmn = xlsx[xlsx[sí_filter] == 'NO'].reset_index(drop=True)

print(f"\nEstudiantes que reportaron estrés (SI): {len(nm)}")
print(f"\nEstudiantes que no reportaron estrés (NO): {len(nmn)}")

columnas_generales = {
    'Semestre actual':                              'semestre',
    'Edad (en años)':                              'edad',
    'Estrato socioeconómico':                      'estrato',
    'Total de asignaturas (Cadi-cai) matriculados':'num_asignaturas',
    'Promedio académico\xa0':                      'promedio',
    'Ha perdido CAI O CADIS':                      'ha_perdido_cai',
    'Horas promedio de estudio diario':            'horas_estudio',
    '¿Trabaja actualmente?':                       'trabaja',
    '¿Tienes responsabilidades familiares adicionales?': 'responsabilidad_familiar',
    'En la última semana, ¿Cuántas horas promedio ha dormido por noche?': 'horas_sueño',
    'Calidad de sueño':                            'calidad_sueño',
    'Consume frecuente de cafeína o energizantes': 'consume_cafeina',
}
columnas_sisco = {
    'La sobrecarga de tareas y trabajos escolares que tengo que realizar todos los días': 's1',
    'La personalidad y el carácter de los/as profesores/as que me imparten clases':       's2',
    'La forma de evaluación de mis profesores/as (a través de ensayos, trabajos de investigación, búsquedas en Internet, etc.)': 's3',
    'El nivel de exigencia de mis profesores/as':  's4',
    'El tipo de trabajo que me piden los profesores (consulta de temas, fichas de trabajo, ensayos, mapas conceptuales, etc.)': 's5',
    'Tener tiempo limitado para hacer el trabajo que me encargan los/as profesores/as':   's6',
    'La poca claridad que tengo sobre lo que quieren los/as profesores/as':               's7',
    '         Fatiga   crónica (cansancio permanente)          ':                         's8',
    'Sentimientos de depresión y tristeza (decaído)':                                     's9',
    'Ansiedad, angustia o desesperación':                                                 's10',
    'Problemas de concentración':                                                         's11',
    'Sentimiento de agresividad o aumento de irritabilidad':                              's12',
    'Conflictos o tendencia a polemizar o discutir':                                      's13',
    '         Desgano   para realizar las labores escolares       ':                      's14',
    'Concentrarse en resolver la situación que me preocupa':                              's15',
    'Establecer soluciones concretas para resolver la situación que me preocupa':         's16',
    'Analizar lo positivo y negativo de las soluciones pensadas para solucionar la situación que me preocupa': 's17',
    'Mantener el control sobre mis emociones para que no me afecte lo que me estresa':   's18',
    'Recordar situaciones similares ocurridas anteriormente y pensar en cómo las solucioné': 's19',
    'Elaboración de un plan para enfrentar lo que me estresa y ejecución de sus tareas': 's20',
    'Fijarse o tratar de obtener lo positivo de la situación que preocupa':              's21',
}

combinacion = {**columnas_generales, **columnas_sisco}
nm = nm.rename(columns=combinacion)

filtro = list(columnas_generales.values()) + list(columnas_sisco.values())
nm = nm[filtro].copy()

print(f"\nColumnas seleccionadas: {len(nm.columns)}")