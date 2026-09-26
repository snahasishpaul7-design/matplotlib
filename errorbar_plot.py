import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
average = [12, 15, 13, 18]
error = [2, 1, 3, 2]

plt.errorbar(months, average, yerr=error, fmt="o-", capsize=5, color="purple")
plt.xlabel("Month")
plt.ylabel("Average value")
plt.title("Monthly Average with Error Range")
plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
