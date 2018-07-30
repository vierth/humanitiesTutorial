# You can change the dots appearance individually as well (as long as we have 
# info for each point)
import matplotlib.pyplot as plt

myX = [i for i in range(20,30)]
myY = [i for i in range(10,0,-1)]

myY[4] = 12

# Let's add a list of colors for the points. These can be words, rgb values,
# or hex values:
colors = ["blue","magenta","black",'magenta',"black","blue","#ff00ff"
          ,"magenta","0.8","green"]

# provide sizes
sizes = [100,50,80,100,150,20,100,90,120,60]


plt.scatter(myX, myY, s=sizes, c=colors)

plt.title("Scatter Plot")
plt.xlabel("x values")
plt.ylabel("y values")

plt.show()