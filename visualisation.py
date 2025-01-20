'''
Visualisation: Matplotlib
'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, label='1st Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My First Plot')
plt.legend()
plt.show()