"""___________________________________________________________________________________________
|                                                                                             |
|      program to print array of specific range                                               |                                                               
|_____________________________________________________________________________________________|
"""

a = "this is vaibhav."

print(a[8])
print(a[8:15])

#The strip() method removes any whitespace from the beginning or the end:
b = " Hello, World! "
print(b.strip()) # returns "Hello, World!"
print(b) 

#The len() method returns the length of a string:
c = "Hello, World!"
print(len(c))

#The lower() method returns the string in lower case:
d = "Hello, World!"
print(d.lower())

#The upper() method returns the string in upper case:
e = "Hello, World!"
print(e.upper())

#input() method is usefor inputing the string from user
print("Enter your name:")
x = input()
print("Hello, " + x)


#The replace() method replaces a string with another string:
f = "Hello, World!"
print(f.replace("H", "J"))
print(f.replace("W", "H"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
