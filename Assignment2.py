# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:41:10 2021

@author: ilq00444
"""

"""
Problem 1 – 15 pts: Calculate sum: function name should be calc_sum 
You are given a list of numbers in python. Assume that the list consists of at least one number. 
Write a python function that returns the sum of all these numbers. Be sure to write this function 
using only python and not an external package, like NumPy.

Problem 2 – 15 pts: Calculate the mean: calc_mean 
You are given a list of numbers in python. Assume that the list consists of at least one number. 
Write a python function that returns the mean of all these numbers. Be sure to write this function 
using only python and not an external package, like NumPy. 

Problem 3 – 30 pts: Calculate the standard deviation: calc_std 
You are given a list of numbers in python. Assume that the list consists of at least two numbers. 
Write a python function that returns the sample standard deviation of all these numbers. Be sure 
to write this function using only python and not an external package, like NumPy. Below is the 
formula is the sample mean. are the data points in the python list/array. 
N is the total number of points.

Problem 4 – 10 pts: Calculate sum with NumPy: calc_sum_np 
Write a function to compute the sum of a python list of numbers. Be free to use a NumPy 
function within your custom function. Same assumptions for inputs as before. 

Problem 5 – 15 pts: Calculate mean with NumPy: calc_mean_np 
Write a function to compute the mean of a python list of numbers. Be free to use a NumPy 
function within your custom function. Same assumptions for inputs as before. 

Problem 6 – 15 pts: Calculate standard deviation with NumPy: calc_std_np 
Write a function to compute the sum of a python list of numbers. Be free to use a NumPy 
function within your custom function. Same assumptions for inputs as before.

"""
import functools
import math

def calc_sum(list_of_numbers):
    
    #calc using for loop
    sum = 0
    for num in list_of_numbers:
        sum += num
    return sum
    
    """
    # calc using recursion
    if (not(list_of_numbers)):
        return 0
    return list_of_numbers[0] + calc_sum(list_of_numbers[1:])
    """
    """
    # calc using built-in sum method
    return sum(list_of_numbers)
    """
    """
    # calc using reduce
    return functools.reduce(lambda a,b: a+b, list_of_numbers)
    """
    """
    # calc using while loop
    sum = 0
    while (list_of_numbers):
        sum += list_of_numbers[0]
        list_of_numbers = list_of_numbers[1:]
    return sum
    """

def calc_mean(list_of_numbers):
    return calc_sum(list_of_numbers)/len(list_of_numbers)

def calc_std(list_of_numbers):
    mean = calc_mean(list_of_numbers)
    std_list = [(num - mean) ** 2 for num in list_of_numbers]
    return math.sqrt(calc_sum(std_list)/(len(std_list)-1))