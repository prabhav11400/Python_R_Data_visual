dir<-c("north","west","east","south")
is.factor(dir)
factor(dir)
dir2<-c("east","west","north","north")
dir2
factor(dir2)
factor(dir, levels =c("north","west","east","south"),labels = c("N","W","E","S") )
factor(dir, levels =c("north","west","east","south"),exclude = "north" )
factor(dir, levels =c("north","west","east","south"),labels = c("W","E","S") , exclude = "north")

## TO GENERATE FACTOR LABELS IN R
# gl() 3 arguments: n,k,labels
# n= labels nam ke vector me number of elements .
# k= labels nam ke vector me hr element kitni bar repeat hoga.
# labels= c("aman",""prabhav","adi")

v1<-gl(3,4,labels=c("ram","mohan","sohan"))
v1
v3<- c("north","west","east","south")
data<- factor(dir) # data nam ke variable me v3 vector ke factor ko store kr liya.
data
# accessing the elements of factors 
data[3]
data[1]
data[c(2,3)]
data[c(2,4)]
data[-1]
data[5]
data[c(1,2,4)]
## modification 
data[2]
data[2]<-"east"
data[2]
data

## 4functions related to factors
# (1) is.factor(): checks if the input is [present in form of factor or not
is.factor(data)
#(2) as.factor() : converts a vector into factor()
v<-c("aman","adi","shipra")
is.factor(v)
v2<-as.factor(v)
is.factor(v2)
is.factor(v)
#(3) is.ordered(): Input is factor(ordered), or not-factor(not ordered)
is.ordered(v2)
is.ordered(v)
#(4) as.ordered():  unordered vector/factor ko ordered vector/factor me badalata hai
v<-c("aman","adi","shipra")
is.ordered(v)
as.ordered(v)
is.ordered(v)
v3<-as.ordered(v)
is.ordered(v3)
