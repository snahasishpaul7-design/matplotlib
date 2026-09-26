import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
rent = [800, 800, 800, 800]
food = [300, 350, 320, 400]
travel = [100, 150, 120, 180]

plt.stackplot(months, rent, food, travel, labels=["Rent", "Food", "Travel"])
plt.xlabel("Month")
plt.ylabel("Cost")
plt.title("Monthly Expenses")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()
