"""___________________________________________________________________________________________
|                                                                                             |
|      program to print list                                                                  |                                                               
|_____________________________________________________________________________________________|
"""

#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

thislist =["vaibhav","aman","ankit"]
print (thislist)


#Change the second item:
thislist =["vaibhav","aman","ankit"]
thislist[1] = "kartik"
print(thislist)

thislist = list(("vaibhav","aman","ankit"))
print (thislist)

# .append is used for adding in list
thislist = list(("vaibhav","aman","ankit"))
thislist.append("naman")
print (thislist)

# .remove is use for removing 
thislist = list(("vaibhav","aman","ankit"))
thislist.remove("ankit")
print (thislist)

#length of the string
thislist =["vaibhav","aman","ankit"]
print (len(thislist))


"""_____________________________________________________________________________
|    Method 	Description
|    append()	Adds an element at the end of the list
|    clear()	Removes all the elements from the list
|   copy()	Returns a copy of the list
|    count()	Returns the number of elements with the specified value
|    extend()	Add the elements of a list (or any iterable), to the end of the current list
|    index()	Returns the index of the first element with the specified value
|   insert()	Adds an element at the specified position
|    pop()	Removes the element at the specified position
|    remove()	Removes the first item with the specified value
|    reverse()	Reverses the order of the list
|    sort()	Sorts the list
|_________________________________________________________________________________"""