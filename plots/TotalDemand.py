import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['total_demand'], color='blue')
plt.title('Total Electricity Demand Over Time (SA)')
plt.xlabel('Time')
plt.ylabel('Total Demand (MW)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()

