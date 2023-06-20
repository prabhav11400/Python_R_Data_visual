h1<- c(82,46,66,23,41)
barplot(h1)

#(2)
H2<- c(12,35,54,31,41)
M2<- c("feb","march","apr","may","june")
barplot(H2, names.arg=M2,xlab="Months",ylab="Revenue",col="yellow",main="Revenue Bar Chart", border="red")

#(3)
months<- c("jan","feb","mar","apr","apr","may")
regions<- c("west","north","south")
values<- matrix(c(21,32,33,14,95,46,67,78,38,11,23,94,15,16,70),nrow=3,ncol=5,byrow=TRUE)
barplot(values,main="Total Revenue",names.arg=months,xlab="MONTHS",ylab="Revenue",col=c("red","blue","green"))
View(values)
legend("topright",regions,cex=0.9,fill=c("red","blue","green"))


