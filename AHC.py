from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

x = np.array([[1,1], [4,1],[1,2],[3,4],[5,4]])

z = linkage(x, 'complete') # Buat yg complete linkage
# z = lingkage(x, 'single') # Buat yang single linkage

plt.figure(figsize=(25, 10))
plt.title("Dendogram")
plt.xlabel("Fitur X")
plt.ylabel("Fitur Y")
dendrogram(z)
plt.show()