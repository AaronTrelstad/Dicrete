import numpy as np
import random
import matplotlib.pyplot as plt 
import csv

##not right

with open('percentChange.csv') as f:
    reader = csv.reader(f)
    list_change = list(reader)

percentChange = []

for i in range(0, len(list_change)):
    percentChange.append(float(list_change[i][0]))

slides = []
currentSlide = percentChange[0]
for i in range(1, len(percentChange)):
    if currentSlide > 0 and percentChange[i] > 0:
        currentSlide += percentChange[i]
    elif currentSlide < 0 and percentChange[i] < 0:
        currentSlide += percentChange[i]
    else:
        slides.append(currentSlide)
        currentSlide = percentChange[i]

print(slides)  