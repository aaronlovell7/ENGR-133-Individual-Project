# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:03:44 2019

@author: aaron
"""
import tkinter as tk

def setTeam(teamNameInput, teamNames, teamNameEntryVar):
    global teamName
    #teamNameInput = teamNameEntry.get()
    if teamNameInput in teamNames:
        teamName.set(teamNameInput)
    else:
        while teamNameInput not in teamNames:
            teamNameFix = tk.simpledialog.askstring('Invalid Name', 'Please enter a valid team name.')
        
            for i in range(len(teamNames)):
                if teamNameFix == teamNames[i]:
                    teamName.set(teamNameFix)
                    teamNameEntryVar.set(teamNameFix)
                    teamNameInput = teamNameFix