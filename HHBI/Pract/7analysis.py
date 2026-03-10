import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("F:/PRINT/HHBI/data.csv")
print(data)
print(data.head)
d = data.groupby('Category')['Price'].sum()
print(d)
total_Stock = data['Stock'].sum()
print("Total stock:",total_Stock)
d.plot(kind="line", marker="s")
plt.plot(d.index, d.values,marker="s")
plt.grid(True)
plt.show()
