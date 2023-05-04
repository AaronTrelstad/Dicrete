import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
import csv

##copy data into an array
with open('close.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

##make list of closing prices
close = []
for i in range(0, len(data)):
    close.append(float(data[i][0]))

days = len(close)
years = days / 365.0
totalGrowth = (close[0]/close[-1])
growthRate = totalGrowth ** (1/years) - 1

st_dev = statistics.stdev(close)

def random_return():
    daily_return = np.random.normal(growthRate/days, st_dev)
    return 1 + (daily_return / 100)

days = 365
simulations = 10
closingPrices = []

## change this to see Histogram vs Monte Carlo
hist = False

for i in range(simulations):
    priceSeries = [close[-1]]
    for i in range(0, days):
        priceSeries.append(priceSeries[-1] * random_return())
    closingPrices.append(priceSeries[-1])
    if not hist:
        plt.plot(priceSeries)

if not hist:
    plt.savefig("monteCarlo(10sim).png")


if hist:
    plt.hist(closingPrices)
    plt.savefig("closing(10sim)")

expectedClose = sum(closingPrices)/len(closingPrices)
print(expectedClose)





