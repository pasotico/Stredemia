import pandas as pd
from collections import Counter as cont
from imblearn.over_sampling import SMOTE as smote
from sklearn.model_selection import train_test_split as seg
from sklearn.preprocessing import LabelEncoder as co

csv = pd.read_csv("../datos/Processed/producto_fase3.csv")

