a = [67,78,90,56]
print (a)

b = [7,3,4,5]
print (a+b)
print (a == b)
print (a != b)
print (a[0]+b[0])
print (a[0]-b[0])
print (a[0]*b[0])
print (a[0]/b[0])
print (a[0]//b[0])
print (a[0]**b[0])

a = [7,32,4,5]
print (a)
print (a[1:3] + b[1:3])
print (a[-1])

names= ['vaibhav','aman','ankit']
print (names)

value = [9.5,'vaibhav',21]
print (value)

mil = [names , a,b]
print(mil)

a.append(45)
print (a)

a.insert(2,77)
print(a)

a.remove(5)
print(a)

a.pop(1)
print(a)

a.pop()
print(a)

del a [1:]
print(a)

a.extend([56,78,90])
print(a)

print(min(a))
print(max(a))
print(sum(a))

a.sort()
print(a)