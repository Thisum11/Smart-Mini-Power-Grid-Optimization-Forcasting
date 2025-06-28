import pandas as pd
import matplotlib.pyplot as plt

#Loading the cleaned dataset
df = pd.read_csv(r'D:\New folder\Smart-Mini-Power-Grid-Optimization-Forcasting\analysis\dataSet01cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

source = [
    col for col in df.columns
    if 'MW' in col and 'Emission' not in col and 'Pumps' not in col and 'Charging'
]

plt.figure(figsize=(14,7))
for col in source:
    plt.plot(df['date'], df[col], label=col)

plt.title("Electricity Generation by source (SA)")
plt.xlabel('Time')
plt.ylabel('Generation(MW)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sourcesEnergy.png')
plt.show()

