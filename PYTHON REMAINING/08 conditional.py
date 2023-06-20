# program to find the greatest of four numbers
a=[0,0,0,0]
a[0]=int(input("Enter number 1"))
a[1]=int(input("Enter number 2"))
a[2]=int(input("Enter number 3"))
a[3]=int(input("Enter number 4"))
print(a)
a.sort()
print(a[3])

# conditional way to find the biggest number out of given 4 numbers

# passed or not let total marks 50 per subject
m1=int(input("Enter the first number"))
m2=int(input("Enter the second number"))
m3=int(input("Enter the third number"))
p1=m1*100/50
p2=m2*100/50
p3=m3*100/50
pt=(m1+m2+m3)*100/150
if((p1>33)and(p2>33)and(p3>33)and(pt>40)):
    print("Student is Passed ")
else:
    print("Student does not satisfy the minimum criteria to be  passed")

#detecting spam comments
comment=input("Type your comment ")
if(comment=="make a lot of money" or
    comment=="buy now" or
    comment == "subscribe" or
    comment=="Click on the link"):
    print("Spam comment detected")

# talk me mere bare me bat ho rhi hai ya nhi
talk=input("Enter the dialogue")
t=talk.upper()
# print(t)
if ("HARRY" in t):
    print("Yes, they were talking about harry")
else:
    print("NO, they were NOT talking about harry")

a=int(input("enter a number"))
for i in range(1,11):
    # print(5*i)
    # print(str(a)+"X"+str(i)+"=",a*i)
    # print(str(a)+"X"+str(i)+"="+str(a*i))
    print(str(a),"X",str(i),"=",str(a*i))
    print(a,"X",i,"=",a*i)

i=1
while i<=10:
    print(5*i)
    i+=1
    