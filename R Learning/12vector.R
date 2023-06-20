# Methods of creating a vector;
#(1)Using C function
a<- c(3,4,5,1,5,7)
a
#(2)Using the colon operator
b<- -1:5
b
#(3)Sequence function[seq()]
sq1<- seq(1,5)
sq1

sq2<- seq(1,5,by=0.5)
print(sq2)

seq3<- seq(1,4,length.out=5)
seq3
seq4<- seq(10,100,length.out=4)
seq4


##Two ways of vector Implementation=(1)Atomic vector, (2)LIST
#Atomic vectors 4 types
#(1)Numeric Vector
numv<-c(12.3,4.6,6,8,9.0)
numv
class(numv)

#(2)Integer Vector
intv<- c(5,6,1,8,9,7)
intv
class(intv)
intv<- as.integer(intv)
class(intv)

intv2<-c(5L,6L,7L,2L,1L)
class(intv2)
intv2


#(3)Character Vector
charv<-c(1,5,7,8)
charv
class(charv)
charv<-as.character(charv)
class(charv)

charv2<-c('ram',"shyam","23")
class(charv2)

#(4)Logical vector
logv1<- c(TRUE,FALSE)
logv1
class(logv1)

logv2<- c(1,2,3,4,0)
logv2<- as.logical(logv2)
logv2                       ### any nonzero value will be considered as true

##vector indexing starts from 1 , not 0
sequence<-seq(1,5)
sequence[1]
seq[3]
sequence[3]
sequence[5]

##Changing index
char_vec<-c("ram"=12,"shyam"=32,"mohan"=64)
char_vec
char_vec["shyam"]

##changing index to logical 
a1<- c(1,2,3,4,5,6,7)
a1[c(TRUE,FALSE,FALSE,TRUE,TRUE,FALSE,TRUE)]

## vector operations
a1<- c(1,2,3,4,5,6,7)
a2<- c("ram","shyam","mohan","sohan")
a3<- c(a1,a2)
a3
a4<-c(5,6,7,8,1,2,4)
a1+a4
a1-a4
a1*a4
a1/a4
a2[1]
a2[3]
a2[7]
a2[-1]
a2[-2] #Irrespective of python, here -1 index is not the laast element of the list
a2[2:4]
a2[c(2,3)]
a2[c(2,3,2)]


##NAMING OF VECTORS
z<-c("ram","mohan","sohan")
z
names(z)=c("y1","y2","y3")
z["y1"]
z["ram"]
  