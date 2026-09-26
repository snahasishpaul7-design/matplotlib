from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

data_file = Path(__file__).parent / "data" / "sales_data_sample.csv"
df = pd.read_csv(data_file)
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
daily_sales = df.groupby("ORDERDATE")["SALES"].sum()

plt.plot(
    daily_sales.index,
    daily_sales.values,
    color="blue",
    linewidth=2,
    marker="o",
    label="Daily sales",
)
plt.xlabel("Order date")
plt.ylabel("Total sales")
plt.title("Daily Sales Report")
plt.legend(loc="upper left")
plt.grid(color="gray", linestyle=":", linewidth=1)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
