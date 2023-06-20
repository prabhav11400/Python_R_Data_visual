#plot(x,y, main, xlab, ylab, xlim, ylim, axes)
# x= x coordinate of the point
# y= y coordinate of the point
# axes= indicates whether the both axes are drawn on plot or not.
View(mtcars) # a predefined dataframe available in R programming
dim(mtcars)
names(mtcars)

data<- mtcars[,c('wt','mpg')]
View(data)
#plotting the chart for cars with weight between 2.5 to 5, and milage between 15 to 30.
plot(x= data$wt,
     y= data$mpg,
     xlab="Weight",
     ylab="milage",
     xlim=c(2.5,5),
     ylim=c(15,30),
     main="Weight v/s milage")
