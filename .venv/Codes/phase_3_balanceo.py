import pandas as pd
from collections import Counter as cont
from imblearn.over_sampling import SMOTE as smote
from sklearn.model_selection import train_test_split as seg
from sklearn.preprocessing import LabelEncoder

csv = pd.read_csv("../datos/Processed/producto_fase3.csv")

cols_texto = csv.select_dtypes(include=['object', 'string']).columns.tolist()
cols_texto = [c for c in cols_texto if c != 'nivel_estres']
encoders = {}
for col in cols_texto:
    le = LabelEncoder()
    csv[col] = le.fit_transform(csv[col].astype(str))
    encoders[col] = le

X = csv.drop(columns=['nivel_estres', 'puntaje_sisco'])
y = csv['nivel_estres']
print("\n*-*-*-* Distribución SIN SMOTE *-*-*-*-*-")
etiquetas = {0: 'bajo', 1: 'medio', 2: 'alto'}
distribucion = csv['nivel_estres'].value_counts().sort_index()
porcentaje = (distribucion / len(csv) * 100).round(1)
resumen = pd.DataFrame({
    'etiqueta': [etiquetas[i] for i in distribucion.index],
    'cantidad': distribucion.values,
    'porcentaje (%)': porcentaje.values
}, index=distribucion.index)
print(resumen)

X_train, X_temp, y_train, y_temp = seg(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

X_val, X_test, y_val, y_test = seg(
    X_temp, y_temp,
    test_size=0.50,  # mitad de 30% = 15%
    random_state=42,
    stratify=y_temp
)

min_clase = min(cont(y_train).values())
k = min(3, min_clase - 1)

sm = smote(random_state=42, k_neighbors=k)
X_train_bal, y_train_bal = sm.fit_resample(X_train, y_train)

print("\n*-*-*-*- Distribución con SMOTE *-*-*-*-*-")
distribucion_bal = pd.Series(y_train_bal).value_counts().sort_index()
porcentaje_bal = (distribucion_bal / len(y_train_bal) * 100).round(1)
resumen_bal = pd.DataFrame({
    'etiqueta': [etiquetas[i] for i in distribucion_bal.index],
    'cantidad': distribucion_bal.values,
    'porcentaje (%)': porcentaje_bal.values
}, index=distribucion_bal.index)

print(resumen_bal)

train_bal = pd.DataFrame(X_train_bal, columns=X.columns)
train_bal['nivel_estres'] = y_train_bal.astype(int)
train_bal.to_csv('../datos/Processed/train_balanceado.csv', index=False)

val_df = X_val.copy()
val_df['nivel_estres'] = y_val.values
val_df.to_csv('../datos/Processed/validacion_original.csv', index=False)

test_df = X_test.copy()
test_df['nivel_estres'] = y_test.values
test_df.to_csv('../datos/Processed/test_original.csv', index=False)

print("\nArchivos guardados correctamente:")
print(f"  Train balanceado: {len(train_bal)} filas")
print(f"  Validación: {len(val_df)} filas")
print(f"  Test: {len(test_df)} filas")
