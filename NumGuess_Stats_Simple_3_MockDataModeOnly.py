import random
import statistics
import pandas
import numpy as np
import matplotlib.pyplot as plt
# List names for each column on the csv file
dfAll = pandas.read_csv('MockDataCSV.csv')

modeL=list(dfAll['gameMode'])
print(modeL)
modalGame=statistics.mode(modeL)
print(f"The most common game mode was {modalGame}")
print("We can show this in a Barchart")
count0=modeL.count(0)
count1=modeL.count(1)
count2=modeL.count(2)
plt.bar(["Sim","Single","Multi"],[count0,count1,count2])
plt.xlabel("Game Mode")
plt.ylabel("Num of Games")
plt.title("Barchart of Games Mode Played")
plt.show()