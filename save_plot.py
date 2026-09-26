import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
visitors = [120, 150, 135, 190]

plt.plot(months, visitors, marker="o", color="darkcyan")
plt.xlabel("Month")
plt.ylabel("Visitors")
plt.title("Monthly Visitors")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("monthly_visitors.png", dpi=300, bbox_inches="tight")
plt.show()
