import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y, marker="o")
plt.title("A Simple Line Plot")
plt.xlabel("X value")
plt.ylabel("Y value")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
