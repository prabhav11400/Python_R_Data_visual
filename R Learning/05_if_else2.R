x<- 25
if(is.integer(x)){
  print("X is an integer")
}else{
  print("x is not an integer")
}

y<- c("hardwork","is","the","key","of","success")
if("key"%in%y){
  print("key is fond in vector")
}else{
  print("key is not found in vector")
}
if("Key"%in%y){
  print("key is fond in vector")
}else{
  print("Key is not found in vector")
}

num1=readline(prompt="Enter the first number : ")
typeof(num1);
num1=as.integer(num1)
typeof(num1)

num2=readline()
num2=as.integer(num2)
sum=num1+num2;
if(sum>10){
  print("sum is greater than 1")
}else if(sum<10){
  print("Sum is less than 10")
}else{
  print("Sum is equal to 10")
}
