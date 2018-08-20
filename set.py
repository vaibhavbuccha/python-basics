"""___________________________________________________________________________________________
|                                                                                             |
|      program to print tuple functions                                                       |                                                               
|_____________________________________________________________________________________________|
"""
"""
Set

A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
"""

thisset = {"vaibhav","aman","ankit"}
print (thisset)


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 


thisset = set(("apple", "banana", "cherry"))
thisset.add("damson")
print(thisset) 


thisset = set(("apple", "banana", "cherry"))
thisset.remove("banana")
print(thisset) 


thisset = set(("apple", "banana", "cherry"))
print(len(thisset)) 