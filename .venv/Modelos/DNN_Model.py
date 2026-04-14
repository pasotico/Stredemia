import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

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
print(f"Features:      {X_train.shape[1]}")

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