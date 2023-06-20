l1=["mayuri","aryan","gufran","prabhav","manikanta","yash","srijan","charvi"]
for names in l1:
    print("Hi "+names+" Good Morning !")
    print("How are you? \n")

# prime or not
n=int(input("inter a number"))
for i in range(2,n):
    if n%i==0:
        print("No,not a Prime Number")
        break
else:
    print("Yes Prime")


for i in range(2,20):
    print(i)
    if(i==10):
        break

for i in range(2,20):
    print(i)
    if(i==10):
        continue

#Factorial
n=int(input("Enter the number of which factorial you have to find : "))
f=n
for i in range(1,n):
    f=f*i
print("\n",f)

# star patterns
for i in range(1,5):
    print("*"*i) ## ye error nhi dega. balki ye multiply, ye batata hai ki itni bar star chahiye. python ids that ios why easier than C

for i in range(1,8):
    if(i%2!=0):
        print("*"*i) #1,3,5,7 stars different-different rows me print ho jayenge.
    
for i in range(1,10):
    if(1<=i<=2):
        print("*",end="")
    if(i==3):
        print("*")
    if(4<=i<=5):
        if(i==5):
            print(" ",end="")
        else:
            print("*",end="")
    if(i==6):
        print("*")
    if(7<=i<=8):
        print("*",end="")
    if(i==9):
        print("*")

#multiplication table of 5 in reverse order
for i in range(10,0,-1):
 print(5,"X",i,"=",5*i)

print(range(10,0,-2))
for i in range(10,0,-2):
    print(i)