install.packages("RMySQL")

install.packages("DBI")
library(DBI)
library(RMySQL)

#con<- dbConnect(MySQL(),
 #               username="root",
  #              password="",
  #              host="localhost",
   #             dbname="registration form"
    #            )
con<- dbConnect(MySQL(),
                username="root",
                dbName="registration form")
dbListTables(con)

dbListFields(con, "form")

data1<- dbGetQuery(con, "select * from form")
print(data1)

data2<- dbSendQuery(con, "select * from form")
data2

data3<- fetch(rs, n=4)
data3

data4<- fetch(rs, n= -1)
data4
