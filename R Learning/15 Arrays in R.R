v1<- c(1,4,5)
v2<- c(10,20,30,40,50,60)
v3<- array(c(v1,v2),dim=c(3,3,2))
print(v3)
v4<- c(10,20,30,40,50,60,70,80)
v5<-array(c(v1,v4), dim=c(3,3,4))
v5
v6<- array(c(v1,v4),dim=c(2,3,4))
v6
 
##Naming in Rows and Columns
v1<- c(1,4,5)
v2<- c(10,20,30,40,50,60)
col_name<-c("C1","C2","C3")
row_name<-c("R1","R2","R3")
mat_name<-c("mat1","mat2","mat3","mat4")
v3<-array(c(v1,v2),dim=c(3,3,4),dimnames=list(row_name,col_name,mat_name))
v3


v3<- c(1,4,5)
v4<- c(10,20,30,40,50,60)
CN<-c("C1","C2")
RN<-c("R1","R2","R3")
MN<-c("mat1","mat2","mat3","mat4")
v5<-array(c(v3,v4),dim=c(2,3,4),dimnames=list(RN,CN,MN))
print(v5)

##accessing the elements of the array
v1<- c(1,4,5)
v2<-c(10,20,30,40,50,60,70,80)
CN<- c("C1","C2","C3")
RN<- c("R1","R2","R3")
MN<- c("M1","M2")
v3<- array(c(v1,v2),dim=c(3,3,2),dimnames=list(RN,CN,MN))
print(v3)
print(v3[3,,2])#  2nd matrix ka 3rd row
print(v3[3,2,1])# 1st matrix ka 2nd column and 3rd row ka element
print(v3[,3,2])# 2nd matrix ka 3rd column

# (row,column,matrix)---- ye order yad rakho bas

##Manipulation in Arrays
v1<- c(1,2,3)
v2<-c(10,20,30,40,50,60,70,80)
v3<- array(c(v1,v2), dim=c(3,3,2))
print(v3)

v4<-c(7,8,9)
v5<- c(9,20,5,40,7,60,70,7)
v6<- array(c(v4,v5), dim=c(3,3,2))
print(v6)

v7<- v3+v6
print(v7)
