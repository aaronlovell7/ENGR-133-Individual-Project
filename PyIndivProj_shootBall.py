# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Program Description 
	defines function to determine whether shot is missed or made

Assignment Information
	Assignment:     Individual Project Shoot Ball
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
#Imports needed modules
import numpy as np

#Defines function to determine whether or not the shot is made
def shotComplete(passValVector):
    randShot = np.random.randint(1,100)             #Sets randShot to a random value
    shotPercentage = (.3 * sum(passValVector))      #The percentage that the shot will be made is set to a value, increasing with the amount of passes complete
    if randShot < shotPercentage:                   #Checks to see if the random value is less than the shot percentage
        shotResult = "Shot made"                    #Sets the variable to tell the main program that the shot was made
    else:                                           #Runs if the random value is not less than the shot percentage
        shotResult = "Shot missed"                  #Sets the variable to tell the main program that the shot was missed
    return shotResult                               #Returns the variable telling the result of the shot

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''