import matplotlib.pyplot as plt

products = ["Notebook", "Pen", "Bag", "Ruler"]
units_sold = [35, 80, 22, 50]

plt.barh(products, units_sold, color="seagreen")
plt.xlabel("Units sold")
plt.ylabel("Product")
plt.title("Product Sales")
plt.tight_layout()
plt.show()
