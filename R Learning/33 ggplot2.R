library(ggplot2)
df<- mtcars
View(df)
ggplot(df,aes(df$disp,df$hp))+geom_jitter(color=df$gear,size=2)

#point plot
ggplot(df,aes(df$disp,df$hp))+geom_point() #(x,y) ke form me mano aes(,) me
ggplot(df,aes(df$disp,df$hp))+geom_point(color=df$gear) #gear ke according color changed
ggplot(df,aes(df$disp,df$hp))+geom_point(color=factor(gear)) #gear ke according color changed
ggplot(df,aes(df$disp,df$hp))+geom_point(color=df$gear,size=2) 
ggplot(df,aes(df$disp,df$hp))+geom_point(color=df$gear, size=2)+xlim(100,500)+ylim(0,400)
ggplot(df,aes(df$disp,df$hp))+geom_point(color=df$gear, size=2)+xlim(100,500)+ylim(0,400)+
   labs(title="horsse power vs displacement", x="Displacement of vehicle", y="hp of engine of the car")

## box plot
ggplot(df,aes(df$mpg,df$disp))+geom_boxplot() #milage x axis pr rahega and displacement y axis par
ggplot(df,aes(x=df$mpg,y=df$disp))+geom_boxplot()
ggplot(df,aes(x=df$mpg,y=df$disp,fill=zygosity))+geom_boxplot()

install.packages(("zyogosity"))
## violine plot
ggplot(df, aes(x=mpg, y=disp))+geom_violin()
ggplot(df,aes(x=df$mpg, y=df$disp))+geom_violin(fill="red")
?ggplot()
ggplot(df, aes(x=drat,y=wt))+geom_violin(trim=FALSE,fill="yellow")
ggplot(df, aes(x=drat,y=wt))+geom_violin(trim=TRUE,fill="yellow")
ggplot(df, aes(x=drat,y=wt))+geom_violin(trim=TRUE,fill="yellow")
ggplot(df, aes(x=drat,y=wt))+geom_violin(aes(color=factor(gear)))# gear(3,4,5) ke according different violin plot
ggplot(df, aes(x=drat,y=wt))+geom_violin(aes(color=factor(cyl)))# cyl(4,6,8) ke according different plots

# World Ma
                                         