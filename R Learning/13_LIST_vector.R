## in atomic vectors all the elemets must be of the same dtype but in case of list we can include any type of datatype in a list vector
vec1<-c(8,9,4,7,6)
vec2<-c("ram","shyam","nam")
vec3<- c(TRUE,FALSE)
list1<-list(vec1,vec2,vec3)
list1

list2<- list("ram","sohan",c(1,3,5,7,9),TRUE,FALSE)
list2

##naming of the list
list3<-list(c("ram","shyam","ramesh"),c(56,89,78),list("btech","bse","ba"))
list3 

names(list3)<- c("students","marks","courses")
list3


##Accessing lists
print(list3[3])
print(list3[2])
print(list3[1])

print(list3["marks"])
print(list3["courses"])


print(list3$marks)
print(list3$courses)


## Changing list to vector so that apply arithmatic operations
list5<- list(5:9)
list5
list6<- list(14:18)
list6
#res<- list5+list6; Error in list5 + list6 : non-numeric argument to binary operator
v1<- unlist(list5)
print(list5)
class(list5)
class(v1)

v2<-unlist(list6)
typeof(v2)

res<-v1+v2
res

##to merge lists
mer<- list(list5,list6)
mer
