# -*- coding: utf-8 -*-
"""
task 1:Calculate Area with Conditions 

Write a Python function calculate_area that takes two parameters: length and width. It 
should calculate and return the area of a rectangle. However, add a condition: if the length 
is equal to the width, return "This is a square!" instead of the area. Then, write a program to 
input values for length and width from the user and call the calculate_area function to 
display either the area or the message

@author: hitesh shukla
"""

def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        area_or_message = calculate_area(length, width)

        print(area_or_message)
    except ValueError:
        print("Invalid input. Please enter valid numeric values for length and width.")

if __name__ == "__main__":
    main()