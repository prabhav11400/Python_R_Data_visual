# using ggplot2
library(ggplot2)
# plotting the chart using ggplot() and geom_point
# ggplot(mtcars, aes(x=drat, y=mpg))+geom_point()
# the aes() function inside the geom_piont() function controls the color of the group
View(mtcars)
ggplot(mtcars,aes(x=drat, y=mpg)) + geom_point(aes(color=factor(gear)))
# ye mtcars matrix ke drat vs mpg ka graph hai. but unme bhi ek aur variable gear koinclude kr sakte hain, if points ka color change kr den
# since gear me 3, 4, 5 ka repetition tha, factor me badal dene se unique ho jata hai. only unique elements are stored in factor
ggplot(mtcars,aes(x=drat, y=mpg)) + geom_line()
ggplot(mtcars, aes(x=drat, y=mpg)) + geom_violin()

