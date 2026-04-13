import pandas as pd
import numpy as np
xlsx =  pd.read_excel('../datos/raw/TEST_ ESTRÉS ACADÉMICO(1-322).xlsx')
sí_filter = next(c for c in xlsx.columns if 'Durante el transcurso ' in c)

nm = xlsx[xlsx[sí_filter] == 'SI'].reset_index(drop=True)
nmn = xlsx[xlsx[sí_filter] == 'NO'].reset_index(drop=True)

print(f"\nEstudiantes que reportaron estrés (SI): {len(nm)}")
print(f"\nEstudiantes que no reportaron estrés (NO): {len(nmn)}")