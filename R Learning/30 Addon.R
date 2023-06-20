####################################################
#(1) unlist() function in R takes a list as an argument and returns a vector.
# A list in R contains heterogeneous elements meaning can contain elements of different types whereas
# a vector in R is a basic data structure containing elements of the same data type.

v<- c("a","s",1,TRUE)
class(v)
v1 <- unlist(v)
v1

#(1) R  program to illustrate
# converting list to vector

# Creating a list.
my_list <- list(l1 = c(1, 3, 5, 7),                
                l2 = c(1, 2, 3),                    
                l3 = c(1, 1, 10, 5, 8, 65, 90))   

# Apply unlist R function
print(unlist(my_list))

##################################################

#(2)
#strsplit():  Strsplit(): An R Language function which is used to split 
#                       the strings into substrings with split arguments.
df<-("R is the statistical analysis language")
strsplit(df, split = " ")

df<-"get%better%every%day"
strsplit(df,split = '%')

df<-"all16i5need6is4a9long8vacation"
strsplit(df,split = "[0-9]+")

df<-"You can type q() in Rstudio to quit R"
strsplit(df,split="")

test_dates<-c("24-07-2020","25-07-2020","26-07-2020","27-07-2020","28-07-2020")
test_mat<-strsplit(test_dates,split = "-")
test_mat
##############################################

#(3)
#lapply() 
#The lapply() function helps us in applying functions 
#on list objects and returns a list object of the same length.
#The lapply() function in the R Language takes a list, vector, or data frame as input 
#and gives output in the form of a list object

# Syntax: lapply( x, fun )
# x: determines the input vector or an object.
# fun: determines the function that is to be applied to input data.
# create sample data
names <- c("priyank", "abhiraj","pawananjani",
           "sudhanshu","devraj")
print( "original data:")
names

# lapply() function
print("data after lapply():")
lapply(names, toupper)


####################################################
#(4) apply()
#This function takes matrix or data frame as an argument 
#along with function and whether it has to be applied by 
#row or column and returns the result in the form of a 
#vector or array or list of values obtained.
# Syntax: apply( x, margin, function )
#Parameters:
  
#  x: determines the input array including matrix.
#margin: If the margin is 1 function is applied across row, if the margin is 2 it is applied across the column.
#         function: determines the function that is to be applied on input data.

#create sample data
sample_matrix <- matrix(C<-(1:10),nrow=3, ncol=10)

print( "sample matrix:")
sample_matrix

# Use apply() function across row to find sum
print("sum across rows:")
apply( sample_matrix, 1, sum)

# use apply() function across column to find mean
print("mean across columns:")
apply( sample_matrix, 2, mean)

#########################################################

#(5) sapply()
#Syntax: sapply( x, fun )

#Parameters:
  
 # x: determines the input vector or an object.
#   fun: determines the function that is to be applied to input data.

# create sample data
sample_data<- data.frame( x=c(1,2,3,4,5,6),
                          y=c(3,2,4,2,34,5))
print( "original data:")
sample_data

# apply sapply() function
print("data after sapply():")
sapply(sample_data, max)

#########################################################


#(6)
# tapply() function
#The tapply() helps us to compute statistical measures (mean, median, min, max, etc..)
#or a self-written function operation for each factor variable in a vector.
#  It helps us to create a subset of a vector and then apply some functions to each of the subsets.
# For example, in an organization, if we have data of salary of employees and we want to find the mean
# salary for male and female, then we can use tapply() function with male and female as factor variable gender.

#Syntax: tapply( x, index,  fun )

#Parameters:
  
#  x: determines the input vector or an object.
#index: determines the factor vector that helps us distinguish the data.
# fun: determines the function that is to be applied to input data.

#Example:
  
 # Here, is a basic example showcasing the use of the tapply() function on the diamonds dataset which is provided by the tidyverse package library.
install.packages("tidyverse")
library(tidyverse)
install.packages("devtools")
install.packages("tidyverse")
installed.packages("tidyverse")

install.packages("broom", dependencies = TRUE)
install.packages("tidyverse", dependencies = TRUE)
 