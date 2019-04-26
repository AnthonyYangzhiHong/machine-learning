import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X, Y1)

for x, y in zip(X, Y1):
	plt.text(x+0.4,y+0.05, 'test', ha='center', va='bottom')

plt.xlim(-.5,n)
plt.xticks(())

plt.show()
