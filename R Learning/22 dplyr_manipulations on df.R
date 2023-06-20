test<- read.csv("/home/prabhav/Music/Dataset.csv")
View(test)
head(test)
tail(test)
names(test)
library(dplyr)
#(1) select() function
sleepdata<- select(test,ID,GENE_SYMBOL)
head(sleepdata)
sleepdata
test1<- select(test, -GENE_SYMBOL)
View(test1)

test2<- select(test, ID:GENE_SYMBOL)
print(test2)
head(select(test,ID:GENE_SYMBOL))

test3<- select(test,starts_with("GE"))
View(head(test3))

test4<- select(test, ends_with("ion"))
print((head(test4)))

test5<- select(test, contains("ID"))
test5

test6<- select(test, matches("GENE")) 
print(test6)

test7<- select(test, one_of(" GENE_SYMBOL","ID"))
test7

#(2) filter() function
names(test)
filter(test, EXPRESSION>9)
filter(test, ENTREZ_GENE_ID<5000,EXPRESSION>9)
filter(test, ID %in% c("117_at","121_at"))
install.packages("magrittr")
library(magrittr)
test %>% head %>% select(ID, GENE_SYMBOL) #functions will execute from left to right. pahle head(first 6 rows), fir ID, GENE_SYMBOL nam ki do column select ho jayenge, jin par head apply ho jayega
test %>% select(ID, GENE_SYMBOL) %>% head # pahle do column selected, then head applied to take first 6 rows only.

# arrange(col1, col2, col3,....) function. 'col1' ko alphabetical order me lagakar, baki select() dvara selected columns ke rows ko rearrange kr deta hai. 

test%>% select(ID,GENE_SYMBOL,EXPRESSION)%>%arrange(EXPRESSION)%>% head #(1)selected 3 columns=>(2)then EXPRESSION is arranged in increasing number. Char hota to alphabetically lagta
test%>% select(ID,GENE_SYMBOL,EXPRESSION)%>%arrange(EXPRESSION,GENE_SYMBOL)%>% head#(1) Same as before, first selected given 3 columns, but second yahan bhi EXPRESSION ke according hi rows ka order decide hoga. 2ND ONWORDS ARGUMENTS OF ARRANGE() ARE USELESS
test%>% select(ID,GENE_SYMBOL,EXPRESSION)%>%arrange(GENE_SYMBOL,EXPRESSION)%>% head # after selecting the first three columns, now rows ka order select krne vala GENE_SYMBOL hota hai. GENE_SYMBOL CHAR HONE KE KARAN ALPHABETICALLY LAGEGA, BAKI 2 COLUMNS KE ROWS BHI USI GENE_SYMBOL VALE ROW KE ANUSAR LG JAYENGE
test %>% select(ID,GENE_SYMBOL,EXPRESSION)%>% arrange(ID) # arrange the rows by ID.  (not used head)

#mutate() add a new column in particular dataframe 
test<- test%>% mutate(RandomNumber=EXPRESSION*ENTREZ_GENE_ID)%>%head
test<- test%>% mutate(RandomNumber=EXPRESSION*ENTREZ_GENE_ID)
View(test)

#group_by() : function used to group data by one or more variables.
t1<- group_by(test,ID)
View(t1)
# alternate of above two lines
test %>% group_by(EXPRESSION)
View(test)
t2<- test %>% group_by(EXPRESSION)
print(t2)
