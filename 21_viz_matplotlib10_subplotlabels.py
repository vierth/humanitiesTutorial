# You can add labels and titles to each of the subplots if you like, as long
# as you do it before calling show() or savefige(). You can also set a size
# for the figure
import matplotlib.pyplot as plt

data = [1,2,3,4,5,6,7,8]
data_2 = [4,2,6,1,1,8,9,3]

# You can insert figsize to make the figure a specific size.
# This is a tuple with the width first then the height
figure = plt.figure(figsize=(11,8))
subplot1 = figure.add_subplot(2, 1, 1)

# On this subplot, draw the data in two different styles
subplot1.plot(data, linestyle = '--')
subplot1.plot(data_2,drawstyle='steps')

# Add a subplot to the second row
subplot2 = figure.add_subplot(2, 1, 2)

# Plot the same thing, but switched around
subplot2.plot(data_2, linestyle='--')
subplot2.plot(data, drawstyle='steps')

# The call is a little different to set the title
subplot1.set_title("Numbers!")
subplot2.set_title("More Numbers!")

# You can also change add x and y labels with set_xlabels() and set_ylabels()
# You can also limit the number of ticks with set_xticks()
# set_xticks() takes a list as input [0, 3, 7] would tell the plot to only show
# those tick marks

# We will also change the yticklabels just for fun
subplot1.set_yticklabels(['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J'],
                         rotation = 15)

plt.show()