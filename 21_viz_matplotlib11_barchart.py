# Bar plots are easy to make too, but do require some adjusted thinking
import matplotlib.pyplot as plt
import numpy as np

# get some random data
data = np.random.randint(20,size=15)
figure = plt.figure()
myplot = figure.add_subplot(1, 1, 1)

# First you will need to get an index.
index = [i for i in range(len(data))]
myplot.bar(index, data)
plt.show()