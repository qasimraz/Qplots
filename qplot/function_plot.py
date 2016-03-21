import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_bar(df,x,y):
    pole = []
    for i in np.unique(df.iloc[:, x]):
        pole.append(sum(df[df[df.columns[x]] == i].iloc[:, y]))
    plt.bar(np.unique(df.iloc[:, x]), pole)
    plt.ylabel('Cumulative total current (A) from PV')
    plt.xlabel('Pole Number')
    plt.title('Bar Chart')
    plt.show()