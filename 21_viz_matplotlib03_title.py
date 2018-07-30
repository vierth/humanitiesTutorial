# You should always label the axes and title the plot
import matplotlib.pyplot as plt

myData = [i*2 for i in range(0,10)]
myDataTwo = [i/2 for i in range(0,10)]

plt.plot(myData)
plt.plot(myDataTwo)

# You can add information before you call show()
plt.title("Useless Data")
plt.ylabel("Data")
plt.xlabel("Index")

plt.show()