def percent(marks):
    return(((marks[0]+marks[1]+marks[2]+marks[3])/400)*100)

marks1=[45,50,55,60]
marks2=[30,40,50,60]
percentage1=percent(marks1)
percentage2=percent(marks2)
print(percentage1,percentage2)

a1=input("Enter Name")
def func(a):
    print("Good Day "+a)

func(a1)

#celcius to fahrenheit
def CtoF(C):
    F=9*C/5 +32
    return F
k=CtoF(37)
print(k)

sum1=0
n=int(input("Enter a number upto which we need to find the sum "))
for i in range(1,n+1):
    sum1=sum1+i
print(f"the sum of first {n} natural numbers is {sum1}")


def mysum(n):
    if(n==1):
        return 1
    else:
        return mysum(n-1)+n

k=mysum(5)
print(k)

def star_pattern(n):
    for i in range(n,0,-1):
       for j in range(1,i+1):
         print("*",end="")
       print("\n")
star_pattern(3)

def star_pat(n):
    for i in range(n,0,-1):
        print("*"*i)
star_pat(6)

def table(n):
    for i in range(1,11):
        print(n,"X",i,"=",n*i)

k=table(4)

