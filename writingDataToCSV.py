import random
import csv
def exportData(playerDataL):            
        # name of csv file 
        filename = "whatever.csv"
            
        # writing to csv file 
        with open(filename, 'a',newline='') as csvfile:
            global csvFirstRow
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
            # writing the data rows 
            csvwriter.writerow(playerDataL)
guessCount=0  # initialise variables

for game in range(5):
    playerid="player1"
    target=random.randint(1,10)
    winLose="1"
    guessCountP1=random.randint(1,5)
    
    p1DataL=[playerid,target,guessCountP1,winLose]
    exportData(p1DataL)
