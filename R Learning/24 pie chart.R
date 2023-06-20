#pie(x,labels,main,col,clockwise,radius)
#x= vector
#main= little
# radius=
# col= color
# clockwise=TRUE

#(1)
x<- c(12,35,56,75)
labels<- c("INDIA","UK","JAPAN","USA")
pie(x)

#(2)
x<- c(12,35,56,75)
labels<- c("INDIA","UK","JAPAN","USA")
pie(x,labels)

#(3)
x<- c(12,35,56,75)
labels<- c("INDIA","UK","JAPAN","USA")
colors=c("blue","green","red","orange")
pie(x,labels,main="Country Pie Chart",col=colors)

#(4)
x<- c(12,35,56,75)
labels<- c("INDIA","UK","JAPAN","USA")
pie(x,labels,main="Country Pie Chart",col=rainbow(length(x)))

#(5)
x<- c(12,35,56,75)
labels<- c("INDIA","UK","JAPAN","USA")
colors=c("blue","green","red","orange")
pie(x,labels,main="Country Pie Chart",col=colors, clockwise=TRUE)

#(6)
#legend(position,legend(same as x),fill,cex(size),bg)
#position="topright"
#bg= background color

x<- c(12,35,50,76)
labels<- c("PAKISTAN","SRILANKA","USA","INDIA")
colors=c("blue","green","yellow","red")
legend("topright",c("PAKISTAN","SRILANKA","USA","INDIA"),cex=0.8,fill=colors)
pie(x,labels,main="COUNTRY PIE CHART",col=colors)

#(7) 3D PIE CHART
#pie3D(x,labels,main,col,explod)
#x=vector
#labels=x ke elements ke corresponding names
# explode=0.2,0.4,0.8 , each slices ke beech space, directly proportional to explode value. (explode=visfot/bursting)
install.packages("plotrix")
library(plotrix)
x2<- c(20,65,15,50,45)
lable2<- c("usa","india","china","uk","uae")
pie3D(x2)
pie3D(x2, labels=lable2, explode=0.2, main="COUNTRY PIE CHART")
pie3D(x2, labels=lable2, explode=0.6, main="COUNTRY PIE CHART")
pie3D(x2, labels=lable2, explode=0, main="COUNTRY PIE CHART")

#(8)complete 3d pie with legend and percentage
library(plotrix)
x1<- c(20,65,15,50,45)
lable1<- c("usa","india","china","uk","uae")
pie.percent<- round(100*x1/sum(x1) ,2)
pie3D(x1,labels=pie.percent,main="Country pie chart",col=rainbow(length(x)))
legend("topright",lable1,cex=0.6,fill=rainbow(length(x)))