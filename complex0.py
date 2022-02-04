import math
import cmath 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

Z = 0
F = [ ]

k = 0
m = 25

#plt.style.use('classic')
# make data
X, Y = np.meshgrid(np.linspace(-1.8, 1.8, 500), np.linspace(-1.8, 1.8, 500))

Y = Y*complex(0,1)

for g in range(50):
	Z =  Z**2 + X + Y



# plot
fig, ax = plt.subplots()
ax.imshow(abs(Z), cmap = 'Wistia')

plt.show()
