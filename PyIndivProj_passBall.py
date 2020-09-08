# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Program Description 
	defines function to determine whether pass is completed or failed

Assignment Information
	Assignment:     Individual Project Pass Ball
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

#Defines function to determine whether pass was completed or not
def passComplete(distance):
    randPass = np.random.randint(1,10)          #Sets randPass to a random value
    
    if distance == "short":                     #Checks if the distance entered by user is 'short'
        if randPass > 2:                        #Checks if the randPass value is greater than 2
            completePass = "Pass Completed"     #Sets variable to tell main program that the pass was complete
            passValue = 10                      #The value of a short pass is 10
            return completePass, passValue      #Returns two variables to the main program
        else:
            failedPass = "Pass Failed"          #Sets variable to tell main program that the pass failed
            passValue = 0                       #The value of a failed pass is 0
            return failedPass, passValue        #Returns two variables to the main program
    elif distance == "long":                    #Checks if the distance entered by user is 'long'
        if randPass > 7:                        #Checks if the randPass value is greater than 7
            completePass = "Pass Completed"     #Sets variable to tell main program that the pass was complete
            passValue = 30                      #The value of a long pass is 30
            return completePass, passValue      #Returns two variables to the main program
        else:
            failedPass = "Pass Failed"          #Sets variable to tell main program that the pass failed
            passValue = 0                       #The value of a failed pass is 0
            return failedPass, passValue        #Returns two variables to the main program
        
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''