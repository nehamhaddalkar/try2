import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("F:/PRINT/HHBI/data.csv")

# Define variables
x = data[['Height']]
y = data['Weight']

# Create and train model
model = LinearRegression()
model.fit(x, y)

# Print equation values
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

# Predict
predicted = model.predict(x)

# Plot
plt.scatter(x, y)
plt.plot(x, predicted)
plt.show()


#install libraries C:\Users\Neha Mhaddalkar\AppData\Local\Programs\Python\Python312
#py -m pip install pandas
#py -m pip install matplotlib
#py -m pip install scikit-learn
