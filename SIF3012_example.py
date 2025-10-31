#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program Name: Taylor Series Sine Calculator
# Subject: SIF3012 Computational Physics
# Author: Juan Carlos Algaba
# Metric Number: xxxxxxxxxxx
# email: algaba@um.edu.my
# Date of Creation: Friday October 2rd

# Description:
# This program calculates the sine of an angle given in degrees using the Taylor series approximation.
# It repeatedly adds terms until the required accuracy provided by the user is achieved.
# The user inputs the angle and the desired accuracy.
# The angle in degrees is converted to radians for the calculation.
# The program compares with Python's math.sin result, and indicates when it has finished.

# Variable Descriptions:
# angle_deg (float): The angle input by the user in degrees.
# angle_rad (float): The angle converted to radians.
# accuracy (float): The desired accuracy threshold for the approximation.
# term (float): Current term in the Taylor series.
# sine_approx (float): The cumulative sum approximating sine(angle_rad).
# n (int): The current term index used to calculate the next term in the series.
# math_sin (float): The actual value of the sine calculated with python math.
# sign (int): Alternates between +1 and -1 to represent series term signs.

import math

# Prompt the user for the angle in degrees
angle_deg = float(input("Enter the angle in degrees: "))

# Prompt the user for the desired accuracy (a small positive float)
accuracy = float(input("Enter the desired accuracy (e.g. 0.0001): "))

# Convert angle from degrees to radians
angle_rad = angle_deg * math.pi / 180

# Initialize variables for the calculation
sine_approx = 0.0  # Sine approximation starts at 0
term = angle_rad   # First term of the Taylor series (x^1/1!)
n = 1              # Term index starts at 1 (for x^(2n-1))
sign = 1           # First term is positive

# Loop until the absolute value of the current term is less than the desired accuracy
while abs(term) >= accuracy:
    sine_approx += term         # Add the current term to the approximation
    n += 1                      # Increment term index
    sign *= -1                  # Alternate sign for next term
    # Calculate the next term:
    # term = previous term * (-1) * x^2 / ((2n-2) * (2n-1))
    term = term * (-1) * angle_rad * angle_rad / ((2*n-2) * (2*n-1))
      
# Calculate sine using math.sin for comparison
math_sin = math.sin(angle_rad)

# Output the result and comparison
print(f"The sine of {angle_deg} degrees approximated with accuracy {accuracy} is: {sine_approx}")
print(f"The sine of {angle_deg} degrees using math.sin is: {math_sin}")
print(f"Difference between approximation and math.sin: {abs(sine_approx - math_sin)}")

print("Program finished.")

#end of the program