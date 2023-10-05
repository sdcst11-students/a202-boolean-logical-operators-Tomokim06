#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer

Enter a number: 2.4
2.4 is not a positive integer

Enter a number: 5
5 is a positive integer

Enter a number: 4.0
4.0 is a positive integer
"""

import math
q = ("Enter a number: ")
a = float(input(q))

if a == 0:
    print("0 is an integer, but it's neither positive nor negative.")
else:
    if a - abs(a) == 0:
        print(f"{a} if a positive integer.")
    else:
        print(f"{a} if not a positive integer.")