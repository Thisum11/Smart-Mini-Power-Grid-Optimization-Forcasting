# Importing the relevant python libraries.

import pandas as pd
import matplotlib.pyplot as plt

#Importing the data sheet
file_path = r'D:\New folder\Smart-Mini-Power-Grid-Optimization-Forcasting\data\202506OpenElectricity.csv'

df = pd.read_csv(file_path)
print(df.head())
print(df.columns)
