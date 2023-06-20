# in simple words, DATAFRAME==TABLE with a header
employ_data=data.frame(
  employee_id=c(1:5),
  employee_name=c("ram",'kam',"nam","A",'B'),
  salary=c(10,20,"no",40,50),
  starting_date=as.Date(c("2012-01-01","2013-01-01","2014-01-01","2015-01-01","2016-01-01"))
  #stringAsFactors=FALSE #to use data frame in machine learning
)
print(employ_data)

str(employ_data)

## Extracting Data in Data Frames

#extract a specific column
f1<-data.frame(employ_data$employee_name)
f1
f2<-data.frame(employ_data$employee_name, employ_data$salary)
f2

#extracting a specific row
f3<- employ_data[2,]
f3
f4<- employ_data[2:4,]
f4

#extracting specific elements
f5<- employ_data[c(2,3),c(1,4)]  # it will extract 2nd and 3rd row, and 1st and 4th column in f5, from f
f5
f6<-employ_data[c(2,3,4),c(1,2,3)] # 2,3,4th rows and 1,2,3rd columns
f6
f7<-employ_data[c(2,3)] # it will etract 2nd and 3rd columns full(all rows)
f7
f8<-employ_data[,c(2,3)] #exactly same as f7, f7 and f8 both  are alternate methods of f1 or f2.
f8
f9<-employ_data[2,3] #2nd row and 3rd column ka intersecting unique element
f9

## Modification in data frame
#(1)Row Addition: rbind()
x<- list(6,"manish",420,"2020-10-12") # list, since all element are of different dtype
rbind(employ_data,x)
x2<-rbind(employ_data,x) #new dataframe is permanentaly stored in x2, withoult doing any changes in actual dataframe
x2
employ_data
#(2) Column Addition: cbind()
y<- c("Ame","pbh","rbl","lko","cnb") #vector, since all element are of same dtype
cbind(employ_data,Address=y)
emp_data_2<-cbind(employ_data,Address=y)
emp_data_2
employ_data
# (3) Row Deletion
deleted_dataframe1<-employ_data[-2,] # 2nd row will be deleted. the deleted dataframe will be stored in new dataframe
deleted_dataframe1
employ_data
#(4) Column Deletion 
employ_data$starting_date<-NULL #here original dataframe se null kiya gya column permanentally delete ho jayega
print(employ_data)
employ_data
x2 # thank GOD i made the backup to store original dataframe

## Summary of datatype
print(summary(x2))
