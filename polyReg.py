import csv
import numpy as np
import matplotlib.pyplot as plt

days = 30

with open('close.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

##make list of closing prices
close = []
for i in range(0, len(data)):
    close.append(float(data[i][0]))

x = []
for idx, num in enumerate(close):
  x.append(idx + 1)

n = 3
mymodel = np.poly1d(np.polyfit(x[-days:], close[-days:], n))

plt.scatter(x[-days:], close[-days:])
plt.plot(x[-days:], mymodel(x[-days:]))
plt.savefig("poly_regDayOpen(2).png")