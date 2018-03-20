import pylab as a
import numpy as b
 
# setting the x - coordinates
x = b.arange(0, 2*(b.pi))
# setting the corresponding y - coordinates
y = b.sin(8*x)
 
# potting the points
a.plot(x, y)
 
# function to show the plot
a.show()
