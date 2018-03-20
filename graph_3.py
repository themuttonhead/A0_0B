import pylab as a
 
# defining labels
activities = ['eat', 'sleep', 'work', 'play']
 
# portion covered by each label
slices = [1, 3, 4, 2]
 
# color for each label
colors = ['r', 'y', 'g', 'b']
 
# plotting the pie chart
a.pie(slices, labels = activities, colors=colors, 
        startangle=60, shadow = False, explode = (0.05, 0.06, 0.1, 0.07),
        radius = 1.0, autopct = '%1.2f%%')
 
# plotting legend
a.legend()
 
# showing the plot
a.show()

