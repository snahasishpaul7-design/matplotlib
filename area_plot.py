import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [12, 15, 13, 18, 22]

plt.fill_between(months, revenue, color="cornflowerblue", alpha=0.4)
plt.plot(months, revenue, color="royalblue", marker="o", label="Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (thousands)")
plt.title("Monthly Revenue")
plt.legend()
plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
