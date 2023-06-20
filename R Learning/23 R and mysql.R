library(RMySQL)
library(DBI)
con1<- dbConnect(MySQL(),
                 username="root",
                 dbname="rigistration form")
dbListTables((con1)) # returns table name i.e. form (only send)
dbListFields(con1 , "forms")# returns attributes/variable names
data1<- dbGetQuery(con1,"select * from form")
data1 # send+fetch , pri table, complete df aa jayegi.
data2<- dbSendQuery(con1,"select * from form")
data2# only variable name aayega, koi df nhi aayega
data3<- fetch(data2, n=-1) # all rows will be preinted
View(data3)
data4<- fetch(data2, n=3) # only first 3 rows will be printed, i.i. will be stored in data4
View(data4)
