v<- c(18,22,28,7,31,52)
plot(v)

#(4)
v<- c(13,22,28,7,31)
w<- c(11,13,32,6,35)
x<-c(12,22,15,34,35)
plot(v,type="o",col="green",xlab="months",ylab="Temperature") #"o"= point and line, #"l"= only line, #"p"= only point
lines(w,type="o",col="red")
lines(x,type="o",col="blue")
# to draw multiple lines use lines() function.