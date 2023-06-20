library(ggplot2)
###########FIRST EVERYTHING OF SINGLE VARIABLE ONLY ##################


#area plot sv(single variable)
sv1<-read.csv("/home/prabhav/Downloads/CompanyABCProfit.csv")
ggplot(sv1,aes(sv2$Profit))+geom_area(fill="red",stat="bin")
dotchart(sv1$Profit)
plot(sv1$Year,sv1$Profit,ylim=c(-500,5000),xlim=c(1800,2050),type="o")
hist(sv1$Profit)
barplot((sv1$Profit))
### so area chart is actually histogram[frequencies(y axis) vs continuous column values(x axis)] chart connected with lines. MORE ACCURATE HISTOGRAM
ggplot(sv1,aes(sv2$Profit))+geom_area(fill="red",stat="bin")
ggplot(sv1,aes(Profit))+geom_area(fill="red",stat="bin")+theme_classic()
ggsave("area.png",width=10,height=8)

## density plot
ggplot(sv1,aes(Profit))+geom_density(size=1)+theme_classic()

## dot plot
ggplot(sv1,aes(Profit))+geom_dotplot()

## HISTOGRAM PLOT
ggplot(sv1, aes(Profit))+geom_histogram()
ggplot(sv1, aes(Profit))+geom_histogram(binwidth=10)
ggplot(sv1, aes(Profit))+geom_histogram(binwidth=10,fill="red")
ggplot(sv1, aes(Profit))+geom_histogram(binwidth=10,fill="red",color="black")
ggplot(sv1,aes(sv1$Profit))+geom_histogram(binwidth=10,fill="red",color="black")+
                           labs(title = "PROFIT VS FREQUENCY OF THAT SPECIFIC PROFIT",x="PROFIT AMOUNT", y="frequency")+
                           theme_classic()
