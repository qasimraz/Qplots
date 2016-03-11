import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import func

df = pd.read_csv('day.csv') # take data from csv make table

time_average1 = []
time_average2 = []
for i in xrange(30):
    time_average1.append(np.mean(df[df['Time'] == i+1].iloc[:, 12]))
    time_average2.append(np.mean(df[df['Time'] == i+1].iloc[:, 13]))
plt.plot(xrange(30), time_average1)
plt.plot(xrange(30), time_average2)
plt.ylabel('Average PV Current (A)')
plt.xlabel('Time (Day)')
plt.title('Solar Energy vs Time')
plt.show()

pole_total = []
for i in np.unique(df.iloc[:, 0]):
    pole_total.append(sum(df[df['Name'] == i].iloc[:, 7]))
plt.bar(np.unique(df.iloc[:, 0]), pole_total)
plt.ylabel('Cumulative total current (A) from PV')
plt.xlabel('Pole Number')
plt.title('Solar Energy vs Poles')
plt.show()
