import numpy as np
from matplotlib import pyplot as plt

date = np.random.randint(-100,50,100)

bins= np.arange(-100,50,3)

plt.xlim([min(date)-5, max(date)+5])

plt.hist(date, bins, alpha=0.5)
plt.title('Salom gahahha')
plt.xlabel("vertex")
plt.ylabel("xayir")
plt.show()