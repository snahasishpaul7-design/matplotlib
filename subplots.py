import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(months, [10, 14, 12, 18], marker="o", color="blue")
axes[0].set_title("Visitors")
axes[0].set_ylabel("People")

axes[1].bar(months, [5, 7, 6, 9], color="orange")
axes[1].set_title("Orders")
axes[1].set_ylabel("Orders")

axes[2].pie([5, 6, 8, 5], labels=months, autopct="%1.1f%%", colors=["gold", "skyblue", "lightgreen", "coral"])
axes[2].set_title("Monthly Orders")

fig.suptitle("Monthly Results")
fig.tight_layout()
plt.show()
