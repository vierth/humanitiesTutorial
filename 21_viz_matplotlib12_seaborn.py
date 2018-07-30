# The seaborn library makes this slightly easier (and even lets us stylize the
# resulting plot, if we don't like the old-fashioned look of matplotlib)
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# set the style to seaborn's own defaults:
sns.set()


# get some random data
data = np.random.randint(20,size=15)
index = [i for i in range(len(data))]
sns.barplot(index,data)


plt.show()