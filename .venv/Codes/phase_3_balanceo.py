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

X_train, X_test, y_train, y_test = seg(
    X, y, test_size=0.30, random_state=42, stratify=y
)