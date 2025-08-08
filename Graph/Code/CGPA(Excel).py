import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Excel ফাইল থেকে ডেটা পড়া
df = pd.read_excel('C:/Users/My PC/Downloads/student_cgpa.xlsx')

names = df['Name'].tolist()
cgpas = df['CGPA'].tolist()

x = np.arange(len(names))
y = np.array(cgpas)

# Smooth curve তৈরি
x_smooth = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

plt.figure(figsize=(10, 5))
plt.plot(x_smooth, y_smooth, color='blue', linewidth=1.5)
plt.scatter(x, y, color='red', s=50, zorder=5)

# CGPA মান পয়েন্টের পাশে লেখা
for i, val in enumerate(cgpas):
    plt.text(x[i], y[i] + 0.05, f"{val:.2f}", ha='center', va='bottom', fontsize=9, color='black')

plt.xticks(x, names)
plt.title("Student CGPA in Semester 1")
plt.xlabel("Student Name")
plt.ylabel("CGPA")
plt.ylim(0, 4.2)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
