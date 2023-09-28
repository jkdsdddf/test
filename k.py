# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset 
data = pd.read_csv('data.csv')

# Exploratory data analysis
print(data.shape)
print(data.describe())
