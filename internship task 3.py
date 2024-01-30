# -*- coding: utf-8 -*-
"""
task 3:
    Write a Python program that generates the Fibonacci sequence up to a specified number of 
terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the 
sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the 
user to enter the number of terms (n) they want in the sequence and then display the 
Fibonacci sequence up to that number of terms

@author: shukl
"""

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

def main():
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))

        if n <= 0:
            print("Please enter a positive integer for the number of terms.")
        else:
            fibonacci_sequence = generate_fibonacci(n)
            print("Fibonacci Sequence up to {} terms:".format(n))
            print(fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of terms.")
if __name__ == "__main__":
    main()