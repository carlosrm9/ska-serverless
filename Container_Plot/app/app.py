import matplotlib.pyplot as plt
import numpy as np

data= np.genfromtxt('/home/app/data/data.txt')
x = data[:,0]
y = data[:,1]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('/home/app/data/Figure.png')
print('Plot generated succesfully')
