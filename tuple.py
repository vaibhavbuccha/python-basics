"""___________________________________________________________________________________________
|                                                                                             |
|      program to print tuple functions                                                       |                                                               
|_____________________________________________________________________________________________|
"""
"""
Tuple

A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
"""
thistuple =["vaibhav","aman","ankit"]
print (thistuple)

thislist =["vaibhav","aman","ankit"]
print (thislist[1])

thistuple =["vaibhav","aman","ankit"]
thistuple[1] = "kartik"
print(thistuple)


thistuple = tuple(("vaibhav","aman","ankit"))
print (thistuple)

thistuple = tuple(("vaibhav","aman","ankit"))
print(len(thistuple))
