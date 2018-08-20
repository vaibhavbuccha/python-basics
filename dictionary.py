"""___________________________________________________________________________________________
|                                                                                             |
|      program to print dictonary functions                                                   |                                                               
|_____________________________________________________________________________________________|
"""
"""
Dictionary

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
"""

thisdict = {
    "name":"vaibhav",
    "fathers_name":"Mr.Dalchand buccha",
    "form":"bikaner"
}
print(thisdict)



thisdict = {
    "name":"vaibhav",
    "fathers_name":"Mr.Dalchand buccha",
    "form":"bikaner"
}
thisdict["name"]="aman"
print(thisdict)

#It is also possible to use the dict() constructor to make a dictionary:
thisdict = dict(apple="green", banana="yellow", cherry="red")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = dict(apple="green", banana="yellow", cherry="red")
thisdict["damson"] = "purple"
print(thisdict)


#Removing a dictionary item must be done using the del() function in python:
thisdict = dict(apple="green", banana="yellow", cherry="red")
del(thisdict["banana"])
print(thisdict)


#The len() function returns the size of the dictionary:
thisdict = dict(apple="green", banana="yellow", cherry="red")
print(len(thisdict))