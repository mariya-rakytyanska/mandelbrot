import math
import cmath 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm



k = 0
m = 25

#plt.style.use('classic')
# make data
X, Y = np.meshgrid(np.linspace(-2.2, 0.9, 2000), np.linspace(-1.8, 1.8, 2000))

Y = Y*complex(0,1)
Z = np.zeros_like(Y)
G = np.zeros_like(X)



for g in range(50):
	Z =  Z**2 + X + Y
	G[(abs(Z)>=2) & (G == 0)]= g
				


# plot

plt.set_cmap("CMRmap")
fig, ax = plt.subplots()
ax.imshow(G)
plt.show()
