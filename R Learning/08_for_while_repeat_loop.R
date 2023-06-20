## for loop
for (variable in vector) {
  
}

for(y in 1:10){
  print(y)
}
for(y in 1:10){
  print(paste()) ## paste() used in string concat
}

f<- c("apple","pie","order")
for(i in f){
  print(i)
  print(f)
}

## repeat loop: no condition loop
v<- c("hello","how","are","you")
x<- 2
repeat{
  print(v)
  x=x+1;
  if(x==20){
    break;
  }
}

## while loop: conditional loop, condition needs to be mentioned earliar irrespective of for loop
v<- c("hello","R","Programming","language")
x<- 10;#initialization of x, nothing but a loop variable.
while(x<20){
  print(v)
  print("loop runned: ")
  print(x-9);
  print("times")
  x=x+1;
}
print(paste("hello hhg","kfk","234"))
print(4+5)
 