#dtype-->numerical value
num1<-as.numeric(26L)
num1
num2<-as.numeric(25-6i)
num2
num3<-as.numeric(TRUE)
num3;
as.numeric(FALSE)
as.numeric("string")
as.numeric( "1234")

#dtype-->integer
int1<-as.integer(53.8854)
int1
as.integer(45-56i)
as.integer(TRUE)
as.integer(FALSE)
as.integer("1234")
as.integer("1234abcd")

#dtype--> complex
comp1<-as.complex(45L)
comp1
as.complex(FALSE)
comp2<-as.complex("1234abcd")
comp3<-as.complex("1234")
comp3

#dtype--> logical
as.logical(45L)
as.logical(-45)
as.logical(0)
as.logical("abcd")
as.logical("1234")
as.logical(0+5i) 
#dtype-->character
char1<-as.character(12)
as.character(TRUE)
as.character(5+6i)
