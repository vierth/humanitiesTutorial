# You can save the figure to file instead of showing
import matplotlib.pyplot as plt

myData = [i*2 for i in range(0,10)]
myDataTwo = [i/2 for i in range(0,10)]

plt.plot(myData)
plt.plot(myDataTwo)

plt.title("Useless Data")
plt.ylabel("Data")
plt.xlabel("Index")

# Save to file here. You can specify many file types, but I recommend using 
# pdf or another vector format so you can edit the figure in a program like
# illustrator
plt.savefig("myFigure.pdf")