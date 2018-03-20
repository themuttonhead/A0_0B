# importing the required module
import pylab
 
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
# plotting the points 
pylab.plot(x, y)
 
# naming the x axis
pylab.xlabel('x - axis')
# naming the y axis
pylab.ylabel('y - axis')
 
# giving a title to my graph
pylab.title('My first graph!')
 
# function to show the plot
pylab.show()