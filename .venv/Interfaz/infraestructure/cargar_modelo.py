import tensorflow as tf
import joblib

@st.cache_resource
def cargar_modelo():
    modelo  = tf.keras.models.load_model('../Modelos/stredemia_modelo.keras')
    scaler  = joblib.load('../Modelos/scaler.pkl')
    return modelo, scaler

