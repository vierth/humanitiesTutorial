# Plotting two lines is just as easy as plotting one:
import matplotlib.pyplot as plt

# Let's create two lists:
myData = [i*2 for i in range(0,10)]
myDataTwo = [i/2 for i in range(0,10)]
# Let's plot it! 
plt.plot(myData)
# Calling plot again will plot the line on the same graph
plt.plot(myDataTwo)

plt.show()
