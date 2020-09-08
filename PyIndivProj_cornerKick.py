# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Program Description 
	defines function to determine whether corner kick is missed or made

Assignment Information
	Assignment:     Individual Project Corner Kick Function
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

#Defines function to determine whether a corner kick is made
def cornerComplete(shotValue):
    if shotValue == "Shot made":                    #Checks to see if the previous shot attempt was made
        resultCorner = "The shot was made"          #Sets the return variable to tell the user that the shot was made
    else:                                           #Runs if the shot was not made
        randCorner = np.random.randint(1,10)        #Sets randCorner variable to a random number
        if (randCorner < 6):                        #If the random number is less than 6, the corner is made
            resultCorner = "The corner was made!"
        else:
            resultCorner = "The corner was missed." #If the random number is not less than 6, the corner was missed
    return resultCorner                             #Returns the variable that tells the main program whether or not the corner was made

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''