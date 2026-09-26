import matplotlib.pyplot as plt

class_a = [65, 70, 72, 75, 80, 85, 90]
class_b = [55, 60, 68, 73, 77, 82, 88]

plt.boxplot([class_a, class_b])
plt.xticks([1, 2], ["Class A", "Class B"])
plt.ylabel("Score")
plt.title("Score Range by Class")
plt.grid(axis="y", linestyle=":", alpha=0.5)
plt.tight_layout()
plt.show()
