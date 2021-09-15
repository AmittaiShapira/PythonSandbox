# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:09:03 2021

@author: ilq00444
"""
import random

def GuessGame():
    mynumber = GetRandomNumberFromLimits()
    count=0
    while True:
        count+=1
        userNumber = int(input("Enter your number: "))
        if(userNumber < mynumber):
            print("too small")
        elif userNumber > mynumber:
            print("too high")
        else:
            print(f"You've got it in {count} tries")
            break # need to break out of infinite loop once answer is given, other keeps looping
            

def GetRandomNumberFromLimits():
     """ inputs the bounds and playing a guessing game"""
     smaller = int(input("Enter the smaller number: "))
     larger = int(input("Enter a larger number: "))
     return random.randint(smaller, larger)
