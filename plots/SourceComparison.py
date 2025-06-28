import pandas as pd
import matplotlib.pylot as plt

#Loading the cleaned dataset
df = pd.read_csv(r'D:\New folder\Smart-Mini-Power-Grid-Optimization-Forcasting\analysis\dataSet01cleaned.csv')
df['date'] = pd.to_datetime(df['date'])