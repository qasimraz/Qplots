import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import func

df = pd.read_csv('data_day_2.27.2016.csv')  # take data from csv make table
weather = pd.read_csv('data_weather.csv')

# The Max Weather Plot
time_average1 = []
weather_data1 = []
weather_data2 = []
for i in range(1, 31):
    time_average1.append(np.mean(df[df['Time'] == i].iloc[:, 11]))
    weather_data2.append(float(weather[weather['Time'] == i].iloc[:, 3]))
    weather_data1.append(float(weather[weather['Time'] == i].iloc[:, 2]))
plt.plot(range(1, 31), df[df['Name'] == 15].iloc[:, 11], label='Max Temp Pole:15', color='orange', alpha=0.7)
plt.plot(range(1, 31), weather_data1, label='Weather Temp High', color='red')
plt.plot(range(1, 31), weather_data2, label='Weather Temp Avg', color='green')
plt.plot(range(1, 31), time_average1, label='Average Max Temp', color='yellow')
plt.ylabel('Temperature')
plt.xlabel('Time (Day)')
plt.title('Average Temperature Max')
plt.legend(loc='upper right', shadow=True)
plt.show()
plt.savefig('plots_png/pole_15_weather_temp.png')

# Min Weather Plot
time_average1 = []
weather_data1 = []
weather_data2 = []
for i in range(1, 31):
    time_average1.append(np.mean(df[df['Time'] == i].iloc[:, 12]))
    weather_data2.append(float(weather[weather['Time'] == i].iloc[:, 3]))
    weather_data1.append(float(weather[weather['Time'] == i].iloc[:, 4]))
plt.plot(range(1, 31), df[df['Name'] == 15].iloc[:, 13], label='Min Temp Pole:15', color='orange', alpha=0.7)
plt.plot(range(1, 31), weather_data1, label='Weather Temp Low', color='red')
plt.plot(range(1, 31), weather_data2, label='Weather Temp Avg', color='green')
plt.plot(range(1, 31), time_average1, label='Average Min Temp', color='yellow')
plt.ylabel('Temperature')
plt.xlabel('Time (Day)')
plt.title('Average Temperature Min')
plt.legend(loc='lower right', shadow=True)
plt.show()

pole_total1 = []
pole_total2 = []
for i in list(np.unique(df.iloc[:, 0])):
    pole_total1.append(sum(df[df['Name'] == i].iloc[:, 7]))
    pole_total2.append(np.std(df[df['Name'] == i].iloc[:, 7]))
plt.bar(list(np.unique(df.iloc[:, 0])), pole_total1, align='center')
plt.xticks(list(np.unique(df.iloc[:, 0])))
plt.ylabel('Cumulative Max Current (A) from PV')
plt.xlabel('Pole Number')
plt.title('Current per Pole')
plt.show()
'''
time_average1 = []
time_average2 = []
for i in list(np.unique(df.iloc[:, 0])):
    time_average1.append(np.mean(df[df['Time'] == i+1].iloc[:, 12]))
    time_average2.append(np.mean(df[df['Time'] == i+1].iloc[:, 13]))
plt.plot(xrange(30), time_average1)
plt.plot(xrange(30), time_average2)
plt.ylabel('Temperature')
plt.xlabel('Time (Day)')
plt.title('Average Temperature Max/Min')
plt.show()
'''