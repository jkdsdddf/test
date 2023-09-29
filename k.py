# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset 
data = pd.read_csv('data.csv')

# Exploratory data analysis
print(data.shape)
print(data.describe())

# Visualize data
plt.hist(data['column1'], bins = 20)
plt.boxplot(data['column2'])
plt.scatter(data['column1'], data['column2'])
plt.show()

# Preprocess data
# Handle missing values
data = data.fillna(method='ffill')
