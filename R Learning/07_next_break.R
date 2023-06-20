## Next: just skip one iteration
x<- 1:10 # this means x=1,2,3,4,5,6,7,8,9,10
for(val in x){
  if(val==5){
    next;
  }
  print(val);
}

#break: totally break the loop comes out of the loop
a<-1
repeat{print(a)
  if(a==5){
    break;
  }
  a<- a+1
  }
