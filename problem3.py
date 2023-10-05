#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

import math

q1 = "Enter a number: "
a1 = float(input(q1))

q2 = "Enter a number: "
a2 = float(input(q2))

q3 = "Enter a number: "
a3 = float(input(q3))

if (a1**2) + (a2**2) == (a3**2) or (a1**2) + (a3**2) == (a2**2) or (a2**2) + (a3**2) == (a1**2):
    print(f"{a1}, {a2}, and {a3} form a Pythagorean triple")
else:
    print(f"{a1}, {a2}, and {a3} do not form a Pythagorean triple")
