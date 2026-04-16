import tensorflow as tf
import joblib

def cargar_modelo():
    modelo = tf.keras.models.load_model('.venv/Modelos/stredemia_modelo.keras')
    scaler = joblib.load('.venv/Modelos/scaler.pkl')
    return modelo, scaler
