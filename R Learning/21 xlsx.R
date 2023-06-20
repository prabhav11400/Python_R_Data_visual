any(grepl("xlsx",installed.packages()))
getwd()
setwd("/home/prabhav/R Learning/")

library(readxl)
#install.packages("readxl")
#install.packages("readxl") 
excel_data<- read_excel("source.xlsx")
#install.packages("tidyverse")
excel_data
View(excel_data)
names(excel_data)
dim(excel_data)
summary(excel_data)
View(excel_data)

#adding a new column
excel_data$new_some=excel_data$DIGITS*excel_data$DIGITS
View(excel_data)
# lets try to save the modified table. But it is also in csv formate, by both .table and .csv, chahe jo bhi extension use karo file name me.
write.table(excel_data,"example.xlsx")
write.csv(excel_data,"example2.xlsx")

names(excel_data)
dim(excel_data)
summary(excel_data)
max<-max(excel_data$new_some)
min<-min(excel_data$new_some)
print(max)
print(min)
View(excel_data)

#Retreiving full info of row, knowing only one element.
details1<- subset(excel_data,DIGITS==10)
details1
details2<-subset(excel_data, NUMBER==9876543210)
details2
details3<- subset(excel_data, NUMBER>9000000000) # not a character ka dusprabhav. This won't work well.
details3
details4<- subset(excel_data, DIGITS>=100)# this will work fine
details4
details6<- subset(excel_data, ((DIGITS>100)&(new_some>1000)))
details6
