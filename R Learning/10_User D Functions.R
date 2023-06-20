#function without argument
func1<-function(){
  for(i in 1:5){
    print(i^2)
               }
}
func1()

#function with argument
func2<-function(x,y,z){
  res<-(x+y+z)
  print(res);
}
func2(4,5,6)
func2(x=4,y=5,z=6)

#function with default argument values
func3<- function(x=10,y=20){
  res<- x*y;
  print(res)
}
func3()
func3(5,6)
