import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Sample data: semesters and CGPAs
semesters = np.array([1, 2, 3, 4, 5, 6, 7, 8])
cgpa = np.array([3.5, 3.75, 3.8, 3.9, 3.85, 3.95, 3.9, 4.0])

# Interpolate for smooth curve
x_smooth = np.linspace(semesters.min(), semesters.max(), 300)
spl = make_interp_spline(semesters, cgpa, k=3)  # k=3 for cubic spline
y_smooth = spl(x_smooth)

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(x_smooth, y_smooth, color='blue', linewidth=1.5)  # narrow and smooth
plt.scatter(semesters, cgpa, color='red')  # show actual points
plt.title("CGPA Progress Over Semesters")
plt.xlabel("Semester")
plt.ylabel("CGPA")
plt.ylim(0, 4.2)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
