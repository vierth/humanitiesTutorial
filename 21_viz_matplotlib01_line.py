# Python has many options for data visualization. matplotlib is one of the 
# older and more widely adopted libraries for this. It is designed to act like
# MATLAB. Let's look at the basics:

# we will need a specific module that is traditionally imported like this:
import matplotlib.pyplot as plt

# Most of this tutorial is based on 
# https://matplotlib.org/users/pyplot_tutorial.html

# Plotting a line. This creates a list of integers from 0 to 18
myData = [i*2 for i in range(0,10)]
print(myData)
# Let's plot it! 
plt.plot(myData)
# To see anything, you'll have to call
plt.show()

# You'll notice that the x axis is the index of the list, the y axis are the 
# values in the list

# To move on, you'll need to close the window that opens
