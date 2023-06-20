#  a histogram is a graphical representation of data where data is grouped into continuous number ranges
# and each range corresponds to a vertical bar.
# No space between consecutive bars( bar chart me space hota tha), in hist plot all bars should be attached to each other
# The x axis should represent continuous data in terms of numbers

# hist(v, main, xlab, ylab, xlim, ylim, breaks, col, border)
# v= vector
# main= title of the chart
# xlab= used to describe x axis
# ylab= used to descroibe the y axis
# xlim= x ki range
# ylim= y axis pr range
# breaks= used to mention the width of each bar, eg 5,60,21 etc. break jitna more, width of histogram utni km, data will become more and more accurate and higher lever distinguishment.

#(1)
v<- c(12,24,16,38,21,13,55,17,39,10,60,59,58)
hist(v, xlab="WEIGHT",ylab="FREQUENCY", col="green",border= "red")

#(2)
v<- c(12,24,16,38,21,13,55,17,39,10,60,59,58)
hist(v, xlab="WEIGHT",ylab="FREQUENCY", col="green",border= "red" , xlim=c(0,40), ylim=c(0,3), breaks=5)
hist(v, xlab="WEIGHT",ylab="FREQUENCY", col="green",border= "red" , xlim=c(0,80), ylim=c(0,7), breaks=5)
s