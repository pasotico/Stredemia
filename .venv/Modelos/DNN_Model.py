import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import f1_score
from tensorflow import keras
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, classification_report

tf.random.set_seed(42)
np.random.seed(42)

train    = pd.read_csv('../datos/Processed/train_balanceado.csv')
val      = pd.read_csv('../datos/Processed/validacion_original.csv')
test     = pd.read_csv('../datos/Processed/test_original.csv')

X_train  = train.drop(columns=['nivel_estres'])
y_train  = train['nivel_estres'].values

X_val    = val.drop(columns=['nivel_estres'])
y_val    = val['nivel_estres'].values

X_test   = test.drop(columns=['nivel_estres'])
y_test   = test['nivel_estres'].values

print(f"Entrenamiento: {X_train.shape}")
print(f"Validación:    {X_val.shape}")
print(f"Prueba:        {X_test.shape}")
print(f"Variables de entrada (features): {X_train.shape[1]}")
print(f"  - Ítems SISCO:     21")
print(f"  - Variables contextuales: 12")

normalizar  = StandardScaler()
X_train_sc  = normalizar.fit_transform(X_train)
X_val_sc    = normalizar.transform(X_val)
X_test_sc   = normalizar.transform(X_test)

def construir_modelo(n_entradas):
    modelo = keras.Sequential([
        keras.layers.Input(shape=(n_entradas,)),

        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.3),

        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dropout(0.3),

        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(0.2),

        keras.layers.Dense(3, activation='softmax')
    ])
    modelo.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return modelo

X_pliegue = np.vstack([X_train_sc, X_val_sc])
y_pliegue = np.concatenate([y_train, y_val])

n_entradas  = X_train.shape[1]
k           = 5
skf         = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)

f1_scores = []
historias   = []
print(f"\ninicio de validación cruzada con {k} folds (pliegues)...\n")
for fold, (idx_train, idx_val) in enumerate(skf.split(X_pliegue, y_pliegue), 1):
    print(f"*-*-*-* Fold {fold}/{k} ")

    X_f_train, X_f_val = X_pliegue[idx_train], X_pliegue[idx_val]
    y_f_train, y_f_val = y_pliegue[idx_train], y_pliegue[idx_val]

    modelo = construir_modelo(n_entradas)

    detente = keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=15,
        restore_best_weights=True
    )
    historia = modelo.fit(
            X_f_train, y_f_train,
            epochs=150,
            batch_size=32,
            validation_data=(X_f_val, y_f_val),
            callbacks=[detente],
            verbose=0
        )
    historias.append(historia)

    y_pred_fold = np.argmax(modelo.predict(X_f_val, verbose=0), axis=1)
    f1 = f1_score(y_f_val, y_pred_fold, average='macro')
    f1_scores.append(f1)
    print(f"F1-score en fold {fold}: {f1:.4f}")
print(f"\nF1-score promedio k-folds: {np.mean(f1_scores):.4f} ± {np.std(f1_scores):.4f}")

print("\n*-*-*-*- Entrenamiento de modelo final *-*-*-*-*-")

modelo_final = construir_modelo(n_entradas)

detente_f = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=15,
    restore_best_weights=True
)

historia_f = modelo_final.fit(
    X_pliegue, y_pliegue,
    epochs=150,
    batch_size=32,
    validation_split=0.1,
    callbacks=[detente_f],
    verbose=1
)
print("\n*-*-*-*- Evaluación final sobre datos de prueba *-*-*-*-")
y_pred_final = np.argmax(modelo_final.predict(X_test_sc, verbose=0), axis=1)
print("\nReporte de clasificación:")
print(classification_report(
    y_test, y_pred_final,
    target_names=['bajo', 'medio', 'alto']
))