# You can change the dots appearance by adding some information in the scatter
# call
import matplotlib.pyplot as plt

myX = [i for i in range(20,30)]
myY = [i for i in range(10,0,-1)]

myY[4] = 12

plt.scatter(myX, myY, s=100, c='magenta')

plt.title("Scatter Plot")
plt.xlabel("x values")
plt.ylabel("y values")

plt.show()