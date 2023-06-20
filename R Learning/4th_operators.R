
a <- 7.5
b<- 2
##ARITHMATIC OPERATORS
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%%b)
print(a%/%b)
print(a^b)
#vectors = collection of similar datatypes
c1<- c(8,9,6)
c2 <- c(2,4,5)
print(c1)
print(c2)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1%%c2)
print(c1%/%c2)
print(c1^c2)

##Relational operator
print(a<b)
print(a>b)
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)

print(c1<c2)
print(c1>c2)
print(c1==c2)
print(c1>=c2)
print(c1<=c2)

##logical operator
d<- c(120, 150, 170)
e<- c(175, 80, 107)
d>=90 && e>=90
d>=90 & e>=90
d>=90 || e>=90
d>=90 | e>=90

f<- c(4.5,TRUE,2+5i)
g<- c(2.4,FALSE,4+7i)
h<- c(0,FALSE,9-6i)
f&g
f&&g
f&h
f&&h
f|g
f||g
f|h
f||h
g|h
g||h
print(!b)
print(!a)

##assignment operater: =, <-, ->, <<-, ->>