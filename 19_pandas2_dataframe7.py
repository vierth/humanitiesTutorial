# You can plot this data:
import pandas as pd
from pandas import DataFrame
# We need this for plotting the data. We'll see more of this later!
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv', sep=",")

df = df[df["TMAX"].notnull()] 
df = df[df["TMIN"].notnull()]
df["TAVG"] = df[['TMAX','TMIN']].mean(1)

# The DATE column contains the date of observation, but let's make sure pandas 
# treats the date column as a "date" datatype:
df["DATE"] = pd.to_datetime(df["DATE"])

# Let's plot the max temperature in Rotterdam:
rot = df[df.NAME == "ROTTERDAM, NL"]

# Let's set the date as the index!
rot = rot.set_index("DATE")
rot["TMAX"].plot()
plt.show()