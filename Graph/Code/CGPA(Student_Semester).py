import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Sample data: Each student's CGPA over 4 semesters
students = {
    'Shovon': [3.5, 3.7, 3.8, 3.9],
    'Rafi': [3.2, 3.4, 3.6, 3.7],
    'Nadia': [3.8, 3.85, 3.9, 4.0],
    'Tariq': [3.0, 3.3, 3.35, 3.6]
}

semesters = np.array([1, 2, 3, 4])

plt.figure(figsize=(10, 5))

# Plot each student's CGPA with smooth line
for name, cgpas in students.items():
    cgpa = np.array(cgpas)
    x_smooth = np.linspace(semesters.min(), semesters.max(), 300)
    spl = make_interp_spline(semesters, cgpa, k=3)
    y_smooth = spl(x_smooth)
    plt.plot(x_smooth, y_smooth, label=name, linewidth=1.5)
    plt.scatter(semesters, cgpa, s=20)  # actual points

# Styling
plt.title("Student-wise CGPA Progression Over Semesters")
plt.xlabel("Semester")
plt.ylabel("CGPA")
plt.ylim(0, 4.2)
plt.xticks(semesters)  # showing only semester numbers
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
