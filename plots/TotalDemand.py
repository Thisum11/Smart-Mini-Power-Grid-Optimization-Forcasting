import pandas as pd
import matplotlib.pyplot as plt

#Loading the cleaned data
df = pd.read_csv(r'D:\New folder\Smart-Mini-Power-Grid-Optimization-Forcasting\analysis\dataSet01cleaned.csv')

df['date'] = pd.to_datetime(df['date'])

# To calculate the total demand
if 'total_demand' not in df.columns:
    mw_columns = [col for col in df.columns if col.endswith('- MW')]
    df['total_demand'] = df[mw_columns].sum(axis=1)


plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['total_demand'], color='blue')
plt.title('Total Electricity Demand Over Time (SA)')
plt.xlabel('Time')
plt.ylabel('Total Demand (MW)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('total_demand.png')
plt.show()

