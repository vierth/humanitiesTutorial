# You can create multiple subplots on a single plot to control the appearance 
# of your visualization
import matplotlib.pyplot as plt

data = [1,2,3,4,5,6,7,8]
data_2 = [4,2,6,1,1,8,9,3]

# First create a figure object
figure = plt.figure()

# Add a subplot (here I am saying there are 2 subplots, and to plot this one in
# the first column in the first row)
subplot1 = figure.add_subplot(2, 1, 1)

# On this subplot, draw the data in two different styles
subplot1.plot(data, linestyle = '--')
subplot1.plot(data_2,drawstyle='steps')

# Add a subplot to the second row
subplot2 = figure.add_subplot(2, 1, 2)

# Plot the same thing, but switched around
subplot2.plot(data_2, linestyle='--')
subplot2.plot(data, drawstyle='steps')


plt.show()