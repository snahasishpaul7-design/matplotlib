import matplotlib.pyplot as plt

products = ["A", "B", "C", "D"]
sales = [1000, 1500, 800, 1200]

plt.bar(products, sales, color="orange", label="Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.legend()
plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
