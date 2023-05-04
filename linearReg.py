import csv
import matplotlib.pyplot as plt
from scipy import stats

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

slope, intercept, r, p, std_err = stats.linregress(x[-days:], close[-days:])

def linear(x):
  return slope * x + intercept

mymodel = list(map(linear, x[-days:]))

plt.scatter(x[-days:], close[-days:])
plt.plot(x[-days:], mymodel)
plt.savefig("close30.png")
