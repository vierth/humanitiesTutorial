# If the data you are using is not continous, you can also make it a scatter
# plot
import matplotlib.pyplot as plt

myX = [i for i in range(20,30)]
myY = [i for i in range(10,0,-1)]

myY[4] = 12 # Let's just change a value so it isn't a straight line

plt.scatter(myX, myY)

plt.title("Scatter Plot")
plt.xlabel("x values")
plt.ylabel("y values")

plt.show()