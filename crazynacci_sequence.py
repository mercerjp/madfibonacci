# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:57:23 2020

@author: James

"""

#Crazynacci sequence
#Write an iterative function crazyIter(x) that, given a number (positive integer) x,
#prints in order the xth first numbers in the Crazynacci Sequence.

def crazyIter(x):
    crazy = [0, -1, -2] #set initialising sequence
    resets = 0 #set intial value of resets
    if x <= 0: #specify print values of initialising sequences
        return 0
    elif x == 1:
        print(*[0]) 
    elif x == 2:
        print(*[0, -1], sep = ',') #convert list to just print integers seperated by commas
    elif x == 3:
        print(*[0, -1, -2], sep = ',')
    else:
        for i in range(3, x): #for every number between the 3rd seq and specified x
            length = len(crazy) #make length of sequence object
            n = crazy[length-1] + crazy[length-2] + crazy[length-3] #sum last 1-3 values of sequence
            if n < -125: #if the sum is smaller than -125
                resets += 1 #add to reset counter
                m = resets + 10 #add 10
                crazy.append(m) #add to end of list
            else: 
                crazy.append(n) #otherwise if sum is =>-125 then add to list
    print(*crazy, sep = ',') #print list as intergers seperated by commas

def crazyRecur(x):
    crazy = [0, -1, -2] #set intialising list
    if x == 1: #set first intialising numbers printed
        print(*[0])
    elif x == 2:
        print(*[0, -1], sep = ',')
    elif x == 3:
        print(*[0, -1, -2], sep = ',')
    else:
        recur(crazy, x-3, 0) #call on another function with the list, length -3 (because of initialising values) and resets
        
def recur(crazy, y, resets):
    y -= 1 #count until finish
    length = len(crazy) #specify length object
    n = crazy[length-1] + crazy[length-2] + crazy[length-3] #sum of last three values
    if n < -125:
        resets += 1
        m = resets + 10
        crazy.append(m) #append reset value to list
    else:
        crazy.append(n) #append sum value to list
    if y == 0: #when finished adding to sequence
        print(*crazy, sep = ',') #print list as integers seperated by commas
    else: recur(crazy, y, resets) #call function on itself again if not finished
    
crazyRecur(18)

def stPrinter(n, shape, character, filled, fillCharacter= '*'):
    if shape == 0 and filled == True: #define filled square
        print(str(character)*n) #top of square length print
        for i in range(0, n-2): #middle of square (n-2 because accounting for either side)
            print(str(character)+str(fillCharacter)*(n-2)+str(character)) #fill middle, starting and ending with the characters
        print(str(character)*n) #bottom line
    elif shape == 0 and filled == False: #empty square
        print(str(character)*n) #top square line
        for i in range(0, n-2): #middle of the square
            print(str(character)+" "*(n-2)+str(character)) #fill middle with space, start and end with character
        print(str(character)*n)
    elif shape == 1 and filled == True: #filled triangle
        for i in range(n): #for every row
            for j in range(n): #and every column
                if j == 0 or i == (n-1) or i==j: #define the coordinates of the right angle we want to draw
                    print(str(character), end="") #print what we want, end to stop
                elif i == 0 or j == (n-1) or j>i: #prevent outside of triangle being filled
                    print(" ", end="")
                else:
                    print(end=str(fillCharacter)) #everywhere else, fill with character
            print()
    elif shape == 1 and filled == False: #empty triangle
        for i in range(n): #for every row
            for j in range(n): #and every column
                if j == 0 or i == (n-1) or i==j: #define the coordinates we want to draw
                    print(str(character), end="") #print what we want
                else: #everywhere else
                    print(end=" ") #fill with blank space, doesn't matter if its outside the triangle either
            print()

            #Test:
# stPrinter(30, 1, "J", True, "M")





