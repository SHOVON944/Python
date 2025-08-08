# graph_test.py

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

print("✅ All libraries imported successfully!")

# Sample data
x = np.arange(1, 6)
y = x ** 2

# Matplotlib Line Graph
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', color='blue')
plt.title("Matplotlib Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y = X squared")
plt.grid(True)
plt.show()

# Seaborn Barplot using Pandas DataFrame
data = pd.DataFrame({
    'Day': ['Sat', 'Sun', 'Mon', 'Tue', 'Wed'],
    'Visitors': [120, 230, 180, 90, 160]
})

sns.barplot(x='Day', y='Visitors', data=data)
plt.title("Seaborn Barplot Example")
plt.show()
