# Plotting a single line is not always that useful. We can give plot
# Two lines if we want to plot them against each other
import matplotlib.pyplot as plt

myX = [i for i in range(20,30)]
myY = [i for i in range(10,0,-1)]

myY[4] = 12 # Let's just change a value so it isn't a straight line

plt.plot(myX, myY)

plt.title("New Line")
plt.xlabel("x values")
plt.ylabel("y values")

plt.show()