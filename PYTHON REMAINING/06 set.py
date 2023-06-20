s=set()
print(len(s))

a1=input("Enter the first number ") #this will be in form of string
a1=int(a1)
s.add(a1)

a2=int(input("Enter Number 2 "))
s.add(a2) 
a3=int(input("Enter Number 3 "))
s.add(a3)
a4=int(input("Enter Number 4 "))
s.add(a4)
a5=int(input("Enter Number 5 "))
s.add(a5)
a6=int(input("Enter Number 6 " ))
s.add(a6)
a7=int(input("Enter Number 7 "))
s.add(a7)
a8=int(input("Enter Number 8 "))
s.add(a8)
print(s) # set only stores unique numbers.

s2={4,"4"}
print(s2)
print(len(s2))

s3=set()
s3.add(20)
s3.add(20.0)
print(len(s3))