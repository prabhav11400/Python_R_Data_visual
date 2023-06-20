names(mtcars)
View(mtcars)
boxplot(mtcars$hp)

boxplot(mtcars$hp,
        main="mtcar data frame",
        xlab="X",
        ylab="Y",
        col="orange",
        border="brown",
        horizontal=TRUE
        )


boxplot(mtcars$hp,
        main="mtcar data frame",
        xlab="X",
        ylab="Y",
        col="orange",
        border="brown",
        horizontal=TRUE,
        notch = TRUE
)


boxplot(mtcars$hp,
        main="mtcar data frame",
        xlab="X",
        ylab="Y",
        col="orange",
        border="brown",
       
        notch = TRUE
)


boxplot(mtcars$hp,
        main="mtcar data frame",
        xlab="X",
        ylab="Y",
        col="orange",
        border="brown")
     
   
#Y~X   BOXPLOT OF Y ARRANGED ACCORDING TO DIFFERENT VALUES OF X
boxplot(mpg~cyl, data=mtcars,
        xlab="Quantity of Cylinders in Car",
        ylab="Miles per Gallon",
        main="R Boxplot Example",col="orange",border="brown")
# above boxplot using notch(median line clear)
boxplot(mpg~cyl,
        data=mtcars,
        xlab="Quantities of cylinders",
        ylab="Miles per Gallon",
        main="Boxplot Example",
        notch=TRUE,
        varwidth=TRUE,
        col=c("RED","BLUE","PINK"),
        name=c("HIGH","MEDIUM","LOW"))


