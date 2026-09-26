import matplotlib.pyplot as plt

scores = [55, 62, 67, 70, 71, 72, 75, 78, 82, 90, 95]

plt.hist(scores, bins=5, color="teal", edgecolor="black")
plt.xlabel("Score")
plt.ylabel("Number of students")
plt.title("Student Score Distribution")
plt.tight_layout()
plt.show()
