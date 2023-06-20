#using ggplot2
library(ggplot2)
# plotting th echart using ggplot()& geom_point() functions
ggplot(mtcars, aes(x=drat,y=mpg))+geom_point()
ggplot(mtcars, aes(x=drat,y=mpg))+geom_line()
ggplot(mtcars, aes(x=drat,y=mpg))+geom_point()
#the aes() function inside the geom_point() function, controls the color of the group.
ggplot(mtcars,aes(x=drat,y=mpg))+geom_point(aes(color=factor(gear))) # gear variable to factor me badal diya and factors me repetion nhi hoti hai

