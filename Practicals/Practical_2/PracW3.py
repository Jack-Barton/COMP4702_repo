import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# @title Classification
# load the dataset
data = pd.read_csv("Practicals\Practical_2\w3classif.csv", names=["X1", "X2", "Y"])

# @title X1 vs X2

from matplotlib.colors import ListedColormap

fig = plt.figure()
colours = ListedColormap(['r','b'])
scatter = plt.scatter(data.loc[:,"X1"], data.loc[:,"X2"], c=data.loc[:,"Y"], cmap=colours, label=data.loc[:,"Y"])
plt.legend(*scatter.legend_elements())
plt.ylabel('X1')
plt.xlabel('X2')