import numpy as np
import pandas as pd
import tensorflow as tf
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
