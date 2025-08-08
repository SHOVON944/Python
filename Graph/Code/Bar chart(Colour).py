import matplotlib.pyplot as plt

x = ['A', 'B', 'C']
y = [10, 15, 7]
colors = ['#FF5733', '#33FF57', '#3357FF']  # Different colors for each bar

plt.bar(x, y, color=colors)
plt.title("Colorful Bar Chart", fontsize=14, fontweight='bold', color='navy')
plt.xlabel("Category", fontsize=12, color='darkred')
plt.ylabel("Value", fontsize=12, color='darkred')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Customize the bars further
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.text(xi, yi/2, f"{yi}", ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')

plt.show()