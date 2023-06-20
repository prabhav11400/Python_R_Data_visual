x<--5.6
y<-5.6
print(abs(x))
print(sqrt(x))
print(sqrt(y))
print(ceiling(x))
print(ceiling(y))
print(floor(x))
print(floor(y))# floor means just chota integer, ceil means just bada integer
z<-c(1.5,5.6,8.6)
print(trunc(z))
p<-5
print(sin(p))
print(log(p))
print(log10(p))
print(exp(p)) #e^5
a<-"123456789"
substr(a,3,5)
s1<-"ManisH GehLot"
print(tolower(s1))
print(toupper(s1))
s1
#grep()- searches a pattern
s2<- c('abcd',"bcbd",'abcdbcbd')
pat<- '^abc'
print(grep(pat,s2))
s3<-c('acd','bcd','abcdbcd')
print(grep(pat,s3))
a1<-c(0:10,40)
a1
su<- sum(a1)
print(su)
a2<-c(0:5)
su<-sum(a2)
print(su)
a1<-c(0:10,23,32,15)
a1
su<- max(a1)
print(su)
su<- min(a1)
print(su)
