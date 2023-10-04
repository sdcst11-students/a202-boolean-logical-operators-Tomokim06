#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""


qx = 'Enter a number for "x":'
x = float(input(qx))

qy = 'Enter a number for "y":'
y = float(input(qy))

p = y/x
pi = int(p)


if p == pi and x<y:
    print(f"{x} is a factor of {y}")
else:
    print(f"{x} is not a factor of {y}")

d = x/y
di = int(d)

if d == di and x>y:
    print(f"{y} is a factor of {x}")
else:
    print(f"{y} is not a factor of {x}")