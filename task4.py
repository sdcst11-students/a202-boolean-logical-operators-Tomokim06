#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
You will need to use a logical statement that checks to see if any of the names
matches the input name.  Don't be surprised if there are many and/or connectors.

(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")


q = "What is your name? "
a = input(q)

if a == "Guile" or a == "Blanka" or a == "Christine" or a == "Carol" or a == "Richard" or a == "Daniel" or a == "Chun-Li" or a == "guile" or a == "blanka" or a == "christine" or a == "carol" or a == "richard" or a == "daniel" or a == "chun-li":
    print(f"Hi {a}! you are a VIP!")
else:
    print("You are not a VIP")
