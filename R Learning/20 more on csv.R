stores<- read.table(file="/home/prabhav/BarGraphs/district.csv",header=T,sep=",")
stores
View(stores)
## adding a new column based on manipulations of each row
stores$RandomSum= stores$active*stores$deceased + stores$confirmed - stores$recovered
View(stores)
View(stores$RandomSum)
print(stores$RandomSum)

##Getting maximum and minimum of any column
max1<- max(stores$RandomSum)
print(max1)
min1<- min(stores$RandomSum)
print(min1)

# Fetching the detail of one complete row, providing one one information about the row: subset()
details1<- subset(stores,RandomSum==max(RandomSum))
print(details1)

details2<-subset(stores,deceased==0)
print(details2)

details3<- subset(stores,district=="Mumbai")
print(details3)

detail4<- subset(stores,((recovered==0)&(deceased==3)))
print(detail4)

detail5<-subset(stores,((recovered>=100)&(deceased<=20)))
print(detail5)

# write.csv() , nyi csv file pwd me banana
# sabse phle R code ki help se ek dataframe bana ,lo
#fir us dataframe ko write.csv function ki help se ek nyi file me copy kr do
#done
mat<- matrix(sample(200,180,replace=T),ncol=6) #random matrix generator
df<- data.frame(mat)
print(df)
write.csv(df,"example-data.csv")
