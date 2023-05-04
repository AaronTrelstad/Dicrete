import numpy as np
import random
import matplotlib.pyplot as plt 
import csv
import statistics

with open('percentChange.csv') as f:
    reader = csv.reader(f)
    list_change = list(reader)

percentChange = []

for i in range(0, len(list_change)):
    percentChange.append(float(list_change[i][0]))

percentChange.reverse()

print(len(percentChange))

swing = []
for i in range(0, len(percentChange)):
    if percentChange[i] < 0:
        swing.append('down')
    else:
        swing.append('up')

swings = []
group = []
current = swing[0]
for i in range(0, len(swing)):
    if swing[i] == current:
        group.append(current)
    else:
        swings.append(len(group))
        group = []
        group.append(swing[i])
        current = swing[i]

averageswing = sum(swings)/len(swings)
st_dev = statistics.stdev(swings)
print(averageswing)
print(st_dev)
    
plt.hist(swings)
##plt.savefig("runs.png")
