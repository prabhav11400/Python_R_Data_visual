# barplot(h,xlab,ylab,main,names,arg,col)
# h= is a vector or matrix which contains numeric values use in the bars
# xlab= A label for the x axis
# ylab = a label for the y axis
# main= A title for the bar chart
# names.arg = a vector of names that will appear under each bar
# col= used to give colors to each bars

#(1)
h1<- c(82,46,66,23,41)
barplot(h1)

#(2)
h2<- c(12,35,54,31,41)
m2<- c("feb","march","apr","may","june")
barplot(h2,names.arg=m2,xlab="Months",ylab="Revenue",col="yellow",main="REVENUE BAR CHART", border="red")

#(3)
months<- c("feb","march","apr","may","june")
regions<- c("east","west","north","south")
values<- matrix(c(21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59),nrow=4, ncol=5, byrow=TRUE)
View(values)
barplot(values, main="Total Revenue direction wise", names.arg=months, xlab="Months",ylab="Revenue",col=c("red","blue","yellow","green"))
legend("topright",regions,cex=0.6,fill=c("red","blue","yellow","green"))
# hua kya= staked bar chart
# matrix ka each column, bar chart ka ek full vertical block ban jayega
# and each row of matrix will be the different colored stakes, in each bar.