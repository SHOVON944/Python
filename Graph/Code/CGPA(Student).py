import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Student names and their CGPA in a single semester
names = ['Shovon', 'Rafi', 'Nadia', 'Tariq', 'Jannat']
cgpas = [3.88, 3.320, 3.450, 3.30, 3.85]

# Convert names to numeric positions for X-axis
x = np.arange(len(names))
y = np.array(cgpas)

# Smooth line using interpolation
x_smooth = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x_smooth, y_smooth, color='blue', linewidth=1.5, label="CGPA Line")
plt.scatter(x, y, color='red', s=50, zorder=5)

# Custom X-axis labels (student names)
plt.xticks(x, names)
plt.title("Student CGPA in Semester 1")
plt.xlabel("Student Name")
plt.ylabel("CGPA")
plt.ylim(0, 4.2)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
