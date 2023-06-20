getwd()
setwd("/home/prabhav/R Learning/")

#sorting of vector
v<- c(12,34,56,32,35,98,33,57,14,59,13,21)
v1<-sort(v)
v1
v2<- sort(v,decreasing=T)
print(v2)

order(v) #sorted v ke elements ka original v me jo jo positions the, vo print karega, in the same order as in sorted v
v[order(v)] #original vector in ascending order.
v
rank(v)

## Now reading CSV
store<- read.csv("/home/prabhav/BarGraphs/district.csv")
print(store)
View(store)
print(is.data.frame(store))
print(ncol(store))
print(nrow(store))

#read.csv ka alternative read.table
store2<- read.table(file="/home/prabhav/BarGraphs/district.csv",header=T,sep=",")
store2
View(store2)

# Some functions related to the dataframe
View(store) #to view the full dataset in a very interactive way
fix(store) #opens dataeditor
str(store)
summary(store)  #provides statistical summary collumnwise
names(store) # show all the variable/column names
nrow(store) #total no of row
ncol(store) # total no of col
length(store) #returns no of columns
dim(store) # returns row, columns
colnames(store)# shows the names of each and every columns
head(store) # shows the first 6 rows of the dataframe
tail(store) #shows the last 6 rows of the dataframe

##manipulations some functions
store.3<- store[c(1:2,5,3:4)] #columns 1st, 2nd, 5th, 3rd, 4th ese aayega
names(store.3)
View(store.3)

store.4<- store[c(1:10),] # stores the first 10 rows
View(store.4)
store.5<- store[c(1:15),c(1:3)]# will store 1 to 15 rows and 1 to 3 columns in store.5 permanently
View(store.5)

grep("district", colnames((store))) # returns the position of "district" variable in all variables

