#(1)
v<- c(12,24,16,38,21,13,55,17,39,10,60,59.58)
hist(v,xlab="weight",ylab="FREQUENCY",col="green",border="red")

#(2)
v<- c(12,24,16,38,21,13,55,17,39,10,60,59.58)
hist(v,xlab="weight",ylab="Frequency",col="green",border="red",xlim=c(0,40),ylim=c(0,3),breaks=5)
hist(v,xlab="weight",ylab="Frequency",col="green",border="red",xlim=c(0,60),ylim=c(0,6),breaks=5)
hist(v,xlab="weight",ylab="Frequency",col="green",border="red",xlim=c(0,60),ylim=c(0,6),breaks=30)

