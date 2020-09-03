#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:48:22 2020

@author: addy
"""
# script designed to randomly select the name of a student in the online TAMU Order of Magnitude class to "go up to the board". This script ensures that no one will be selected two weeks in a row.

import random
import os

names = ["Addy", "Micalyn", "Silvana", "Gesa", "Joanne", "Justin", "Kaitlin"]

def randomNameSelector(names):
    filepath = "oomNameSelected.txt"
    
    if os.path.exists(filepath):
        pass
    else:
        with open(filepath,"w+") as file:
            file.write("Randomly selected names for OoM class" + '\n')
    
    with open(filepath, "r") as file:
        lines = file.readlines()
        lastLine = lines[-1].strip()
        nameSelected = lastLine
        randomIndex = random.randrange(0,len(names),1)
        nextIndex = randomIndex - 1
        if names[randomIndex] == nameSelected:
            with open(filepath,"a") as file:
                file.write(names[nextIndex] + '\n')
        else:
            with open(filepath,"a") as file:
                file.write(names[randomIndex] + '\n')
                
randomNameSelector(names)