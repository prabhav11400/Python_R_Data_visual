# Reading .csv file
getwd()
setwd("/home/prabhav/R Learning/")
formate1<-read.csv(file.choose())
head(formate1)
View(formate1)

#reading elsx file
install.packages("readxl")
library(readxl)
formate2<-read_xlsx(file.choose())
head(formate2)

#txt file
formate3<- read.delim(file.choose())
head(formate3)


# bar plot()
?barplot()
bp1<-read.csv(file.choose())
barplot(bp1$X1)
barplot(bp1$X1,ylim=c(0,200))
barplot(bp1$X1,ylim=c(0,200),names=bp1$X) # X is sample number(1 to 30), X1 consider as expression of different genes
barplot(bp1$X1,ylim=c(0,200),names=bp1$X,xlab="Sample Number",ylab="expression level")
barplot(bp1$X1,ylim=c(0,200),names=bp1$X, xlab="Sample Number", ylab="Expression level", main="GENE EXPRESSION", col=c(2,5))
barplot(bp1$X1,ylim=c(0,200),names=bp1$X, xlab="Sample Number", ylab="Expression level", main="GENE EXPRESSION", col=c(2,5,7))
barplot(bp1$X1,ylim=c(0,200),names=bp1$X,xlab="Expression Value", ylab="Sample Number", main="GENE Expression", col=c(2,5,7), horiz=TRUE)

# dot chart
dt<- read.csv("/home/prabhav/example-data.csv")
View(dt)
dotchart(dt$X1)
dotchart(dt$X1, labels=dt$X)
dotchart(dt$X1,labels = dt$X, color="red")
dotchart(dt$X1,labels=dt$X,color="red",pch=16)
dotchart(dt$X1,labels=dt$X, color="red", pch=16,cex=1)
dotchart(dt$X1,labels=dt$X, color="blue",pch=16,cex=1.5,xlab="Sample Anukrank",ylab="Expression lebel", main="Gene expression level")

#pie chart
pt<- read.csv("/home/prabhav/example-data.csv")
pie(dt$X1)

#histogram chart
hist(dt$X1,labels=dt$X,xlab="GENE ID",ylab="GENE EXPRESSION",main="random histogram chart")
hist(dt$X1,labels=dt$X,xlab="GENE ID",ylab="GENE EXPRESSION",xlim=c(0,300),main="random histogram chart")
hist(dt$X1, xlab="GENE EXPRESSION/ X1 COLUMN KI VALUES", ylab="X1 COLUMN VALUES KI DIFFERENT RANGE ME FREQUENCIES",col="red",border="black")

# clustor (x,y) plot
plot(bp1$X, bp1$X1, xlab="Gene Roll Number", ylab="Gene Expression", main="(x,y) or (gene id, gene expression value graph)")
plot(bp1$X, bp1$X1, xlab="Gene Roll Number", ylab="Gene Expression", main="(x,y) or (gene id, gene expression value graph)",pch=12)
plot(bp1$X, bp1$X1, xlab="Gene Roll Number", ylab="Gene Expression", main="(x,y) or (gene id, gene expression value graph)",pch=16)
plot(bp1$X, bp1$X1, xlab="Gene Roll Number", ylab="Gene Expression", main="(x,y) or (gene id, gene expression value graph)",pch=16, cex=2)

# boxplot()
bp2<-read.csv(file.choose())
boxplot(bp2$X1)
boxplot(bp2$X1, bp2$X2, names=c("X1","X2"),col=c(4,6))
boxplot(bp2$X1, bp2$X2, bp2$X3)
boxplot(bp2$X1, bp2$X2, bp2$X3, names=c("X1","X2","X3"), col=c(4,6,8))
boxplot(bp2$X1, bp2$X2, bp2$X3, names=c("X1","X2","X3"), col=c(4,6,8), xlab="gene id or gene", ylab="Expression", main="Y pr column ki values and x par column names")
