# matrix(data, nrow, ncol, byrow, dim_name)
#data= elements that need to be elements of matrix, eg c(1:5), c(1,2,3,4,5,6,7)
#ncow= number of rows
#ncol= number of columns , specify anyone of nrow and ncol, second will be autometically specified
#byrow= FALSE(BY DEFAULT) i.e. bydefault elements ka arrangement columnwise hota hai.
#byrow= TRUE i.e. elements ka arrangement row wise hoga , matlab pahle 1st row puri bharegi , fir 2nd, fir 3rd..
#dimname= (row_name, col_name, matrix_name)
mat1<-matrix(c(2:13),nrow=4,byrow=TRUE)
mat1
mat2<-matrix(c(2:13),nrow=4,byrow=FALSE)
mat2
mat4<-matrix(c(2:13),ncol=4,byrow=TRUE)
mat4
mat3<-matrix(c(2:12),nrow=4,byrow=TRUE)
mat3
mat5<-matrix(c(2:12),ncol=4,nrow=4,byrow=FALSE)
mat5

row_name<- c("R1","R2","R3","R4")
col_name<- c("C1","C2","C3","C4")
z<- matrix(c(7:18),nrow=4,ncol=4,byrow=TRUE,dimnames=list(row_name,col_name))
print(z)

##Accessing the elements of the matrix
print(z[3,1]) #3rd row and 1st column
print(z[4,3]) #4th row 3rd column
print(z[3,]) #pura 3rd row of z
print(z[,2])#pura 2nd column

## Updating or changing elements 
z[4,3]<- 0
print(z[4,3])
z

z[z==11]<- 0  #updating using relational operators
# z matrix me jhan bhi 11 hoga vo 0 ho jayega.
z

z[z>15]<- 0 # 15 se bada jo kuch bhi hai 0 ho jayega
print(z)

#cbind()  to add a coloumn[temporary]
z
cbind(z,c(2,3,4,5))
z
#rbind() to add a temprary row
rbind(z, c(2,3,4,5))
z

##t(z)= transpose matrix of z,  ij--ji of any matrix
z
t(z)
z
