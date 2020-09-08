# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Program Description 
	creates widget, runs other defined functions to create word based soccer game

Assignment Information
	Assignment:     Individual Project Main 
	Author:         Heath Aaron Lovell, hlovell@purdue.edu
	Team ID:        003-15 (e.g. 001-14 for section 1 team 14)
	
Contributor:    N/A
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
#Importing all the needed modules and user defined functions
import tkinter as tk
import numpy as np
import PyIndivProj_passBall as passingBall
import PyIndivProj_shootBall as shootingBall
import PyIndivProj_cornerKick as cornerKick

root = tk.Tk()

#Initialize the team name entry variable
teamNameEntryVar = tk.StringVar()
teamNameEntryVar.set("Enter EPL team name")

#Initialize the pass distance variable
distanceVar = tk.StringVar()
distanceVar.set('"short" or "long" pass')

#Initialize the team name variable
teamName = tk.StringVar()
teamName.set("Your team")

#Initialize the pass complete variable
passComplete = tk.StringVar()
passComplete.set("Pass Results")

#Initialize the pass values vector
passValVector = []

#Initialize the complete shot variable
completeShot = tk.StringVar()
completeShot.set("Shot Results")

#Initialize the corner result variable
cornerResult = tk.StringVar()
cornerResult.set("Corner Kick Results")

#Initialize the list of teams the user can choose
teamNames = ["Arsenal", "Aston Villa", "AFC Bournemouth", "Brighton and Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Sheffield United", "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers"]

#Define the function allowing the user to set the team
def setTeam():
    global teamName
    teamNameInput = teamNameEntry.get()                     #Gets the user input in the team name entry
    if teamNameInput in teamNames:                          #Checks to make sure that the input is in the valid list of team names
        teamName.set(teamNameInput)                         #Sets the team name label to the input from user
    else:
        while teamNameInput not in teamNames:               #Runs loop for when user input is not in the valid list of team names
            teamNameFix = tk.simpledialog.askstring('Invalid Name', 'Please enter a valid team name.')  #Gets new user input, asking for valid team name
        
            for i in range(len(teamNames)):                 #Runs loop for every value in the valid team names list
                if teamNameFix == teamNames[i]:             #Checks to see if the team name is in the valid list of names
                    teamName.set(teamNameFix)               #If the input is valid, it sets the team name variable to the input
                    teamNameEntryVar.set(teamNameFix)       #If input is valid, sets team name entry to input
                    teamNameInput = teamNameFix             #Sets team name input to the valid name
     
#Defines the pass ball function                   
def passBall():
    distance = passDistanceEntry.get()                      #Gets user input for 'short' or 'long' pass
    if distance == "short" or distance == "long":           #Making sure user input is valid 
        passOutput = passingBall.passComplete(distance)     #Sets pass output the the value returned by the function 'passComplete'
        passComplete.set(passOutput[0])                     #Sets the pass complete label variable to the pass output
        passValVector.append(passOutput[1])                 #Sets the pass value vector to the vector returned by the function 'passComplete'
    elif distance != "short" and distance != "long":        #If distance is not valid
        while distance != "short" and distance != "long":   #Loop for when distance is not valid
            newDistance = tk.simpledialog.askstring('Invalid distance.', 'Please enter either "short" or "long".')  #Prompts user to enter a new valid distance
            distance = newDistance                          #Sets distance to the valid distance    
    distanceVar.set(distance)                               #Sets distance entry to distance inputted by user
    
#Defines the shoot ball function
def shootBall():    
    global shotValue
    shotValue = shootingBall.shotComplete(passValVector)    #Sets shot value to the value returned by the 'shotComplete' function
    completeShot.set(shotValue)                             #Sets the complete shot label to the shot value
    
#Defines the corner kick function
def cornerKickBall():
    resultCorner = cornerKick.cornerComplete(shotValue)     #Sets the corner result to the value returned by the 'cornerComplete' function
    cornerResult.set(resultCorner)                          #Sets the corner result label to the corner result
    
#Defines 0 of the widget
teamNameEntry = tk.Entry(root, text = teamNameEntryVar, textvariable = teamNameEntryVar)
changeTeamBtn = tk.Button(root, text='Change Team', command=setTeam)
teamNameLbl = tk.Label(root, text = teamName, textvariable = teamName)

#Defines 1 of the widget
passDistanceEntry = tk.Entry(root, text = distanceVar, textvariable = distanceVar)
passBallBtn = tk.Button(root, text='Pass Ball', command=passBall)
passCompleteLbl = tk.Label(root, text = passComplete, textvariable = passComplete)

#Defines 2 of the widget
shootBallBtn = tk.Button(root, text = 'Shoot Ball', command=shootBall)
shootBallLbl = tk.Label(root, text = completeShot, textvariable = completeShot)

#Defines 3 of the widget
cornerKickBtn = tk.Button(root, text = "Corner Kick", command=cornerKickBall)
cornerKickLbl = tk.Label(root, text = cornerResult, textvariable = cornerResult)

#Organizes row 0 in the widget
teamNameEntry.grid(row=0, column=0)
changeTeamBtn.grid(row=0, column=1)
teamNameLbl.grid(row=0, column=2)

#Organizes row 1 in the widget
passDistanceEntry.grid(row=1, column=0)
passBallBtn.grid(row=1, column=1)
passCompleteLbl.grid(row=1, column=2)

#Organizes row 2 in the widget
shootBallBtn.grid(row=2, column=1)
shootBallLbl.grid(row=2, column=2)

#Organizes row 3 in the widget
cornerKickBtn.grid(row=3, column=1)
cornerKickLbl.grid(row=3, column=2)

root.mainloop()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''