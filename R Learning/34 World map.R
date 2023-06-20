library(maps)
wm<-map_data("world")
View(wm)
ggplot(world_map,aes(x=long,y=lat))+geom_polygon()
ggplot(world_map,aes(x=long,y=lat,group=group))+geom_polygon()
ggplot(world_map,aes(x=long,y=lat,group=group))+geom_polygon(fill="lightgray")
ggplot(world_map,aes(x=long,y=lat,group=group))+geom_polygon(fill="lightgray",color="white")

##Highlight Some Countries##
highlit.some.countries<-c("Sri Lanka","India","Pakistan","Saudi Arabia","Iraq","Iran","Qutar","Turkey","Afganistan","Bangaladesh","Nepal")
highlit.some.countries
highlit.some.countries<-map_data("world",region=highlit.some.countries)
highlit.some.countries
View(highlit.some.countries)

library(dplyr)
require(maps)
require(viridis)
theme_set(
  theme_void()
)

region.lab.data<-highlit.some.countries%>%group_by(region)%>%summarise(long=mean(long),lat=mean(lat))

ggplot(highlit.some.countries,aes(x=long,y=lat))+geom_polygon(aes(group=group,fill=region))

ggplot(highlit.some.countries,aes(x=long,y=lat))+geom_polygon(aes(group=group,fill=region))+
  geom_text(aes(label=region),data=region.lab.data,size=5,hjust=0.5)


ggplot(highlit.some.countries,aes(x=long,y=lat))+geom_polygon(aes(group=group,fill=region))+
  geom_text(aes(label=region),data=region.lab.data,size=5,hjust=0.5)+theme(legend.position="none")

ggplot(highlit.some.countries,aes(x=long,y=lat))+geom_polygon(aes(group=group,fill=region))+
  geom_text(aes(label=region),data=region.lab.data,size=5,hjust=0.5)+scale_fill_viridis_d()

## UPAR KA CODE JINDGI BHAR KAM AAYEGA 2 ,3 OR MORE COUNTRIES KE COMPARISON KARNE ME. KEEP THAT SAFE..
# LETS TRY DIFFERENT SET OF COUNTRIES
highlit.some.countries<-c("India","China","USA","Russia","Austrelia","Japan")
highlit.some.countries
highlit.some.countries<-map_data("world",region=highlit.some.countries)
highlit.some.countries
View(highlit.some.countries)

library(dplyr)
require(maps)
require(viridis)
theme_set(
  theme_void()
)
region.lab.data<-highlit.some.countries%>%group_by(region)%>%summarise(long=mean(long),lat=mean(lat))

ggplot(highlit.some.countries,aes(x=long,y=lat))+geom_polygon(aes(group=group,fill=region))+
  geom_text(aes(label=region),data=region.lab.data,size=5,hjust=0.5)

