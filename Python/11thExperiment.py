# Write programs to understand the use of Matplotlib for Working with Line Chart, Histogram, Bar Chart, Pie Charts.

# LINE CHART

import matplotlib.pyplot as plt
import numpy as np

# Define X and Y variable data
x = np.array([1, 2, 3, 4])
y = x * 2

plt.plot(x, y)
plt.xlabel("X-axis")  # add X-axis label
plt.ylabel("Y-axis")  # add Y-axis label
plt.title("Any suitable title")  # add title
plt.show()

# HISTOGRAM

from matplotlib import pyplot as plt

# Creating dataset
a = np.array([22, 87, 5, 43, 56,
              73, 55, 54, 11,
              20, 51, 5, 79, 31,
              27])

# Creating histogram
fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(a, bins=[0, 25, 50, 75, 100])

# Show plot
plt.show()

# BAR CHART

# creating the dataset
data = {'C': 20, 'C++': 15, 'Java': 30,
        'Python': 35}
courses = list(data.keys())
values = list(data.values())

figs = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='maroon',
        width=0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

# PIE CHART

# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]

# Creating plot
figss = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)

# show plot
plt.show()
