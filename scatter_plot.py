import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6]
test_scores = [45, 52, 61, 70, 78, 88]

plt.scatter(hours_studied, test_scores, color="blue", marker="o", s=80)
plt.xlabel("Study hours")
plt.ylabel("Test score")
plt.title("Study Hours and Test Scores")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
