import numpy as np
import matplotlib.pyplot as plt
import random
from collections import defaultdict

##Markov Chain to predict Google Stock Price

##Intial State
states = ["Increase", "Decrease"]

##Future moves
moves = [["Increase", "Decrease"], ["Increase", "Decrease"]]

##Matrix of movement possiblities (125 total moves from 10/25/2022 to 4/25/2023)
moveChance = [[(31/59), (28/59)], [(29/65), (36/65)]]

## start is if you want the program to begin with increase or decrease
## days if how many days you want to run the program from
def markov(start, days):
    ##Intial condition is a Increase
    currentState = start
    stateList = [currentState]

    counter = 0
    ##prob will store probability of moves
    prob = 1

    ##Increase counter untill it matches the requested number of days
    while counter != days:

        ## If current state is Increase
        if currentState == "Increase":
            ##random move using probabilty from increase
            move = np.random.choice(moves[0], replace=True, p=moveChance[0])
            ##Case : Increase -> Increase
            if move == "Increase":
                prob *= moveChance[0][0]
                stateList.append(currentState)
            ##Case : Increase -> Decrease
            else:
                prob *= moveChance[0][1]
                ##Change current state from Increase to Decrease
                currentState = "Decrease"
                stateList.append(currentState)
        ## If current state is Decrease
        else:
            ##random move using probabilty from increase
            move = np.random.choice(moves[1], replace=True, p=moveChance[1])
            ##Case : Decrease -> Decrease
            if move == "Decrease":
                prob *= moveChance[1][1]
                stateList.append(currentState)
            ##Case : Decrease -> Increase
            else:
                prob *= moveChance[1][0]
                ##Change current state from Decrease to Increase
                currentState = "Increase"
                stateList.append(currentState)
        ##Increase counter
        counter += 1
    return currentState, stateList

##Holds the currentState and stateList that is returned
storage = []

##count is the number of times that the requested state appears in storage
count = 0

##simulations is the number of simulations you wnat to run on the data
simulations = 1000


##request is the moves you want to track
request = "Increase"

##start is the state you want to start at
start = "Increase"

##simulate event 
for interations in range(0, simulations):
    storage.append(markov(start, 2))

##Record numebr of times request occured
for change in storage:
    if change[0] == request:
        count+=1

percentage = (count/simulations) * 100

print("Start State: "+start+" End State: "+request+" = "+str(percentage)+"%")

##Stores all of the paths that move took and their frequencies
paths = defaultdict(list)

##Since we cant use a list a key to a dictionary we need to convert every list to a string
strings = []

storage_paths = []
for i in range(0, len(storage)):
    storage_paths.append(storage[i][1])

for i in range(0, len(storage_paths)):
    path = ""
    for j in range(0, len(storage_paths[i])):
        path += storage_paths[i][j]
    strings.append(path)

##Count how many times each path occurred during teh simulation
for path in strings:
    if path not in paths:
        paths[path] = [1]
    else:
        paths[path][0] += 1

##Find percentage of occurance
for i in strings:
    if paths[i][0]/simulations not in paths[i]:
        paths[i].append(paths[i][0]/simulations)

print(paths)



