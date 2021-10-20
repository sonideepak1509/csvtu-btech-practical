# Write programs to understand the use of Matplotlib for Simple Interactive Chart,
# Set the Properties of the Plot, matplotlib and NumPy.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = x ^ 2

# How to set Properties

#Labeling the Axes and Title

plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")

# Formatting the line colors

plt.plot(x,y,'r')

# Formatting the line type

plt.plot(x,y,'>')

# save in pdf formats

plt.savefig('timevsdist.pdf', format='pdf')
