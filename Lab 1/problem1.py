import numpy as np
import matplotlib.pyplot as plt

set1 = np.random.normal(-10, 5, 1000)
set2 = np.random.normal(10, 5, 1000)

setSum = np.add(set1, set2)

mean = np.mean(setSum)
variance = np.std(setSum)

print(mean)
print(variance)
plt.hist(setSum)
plt.show()