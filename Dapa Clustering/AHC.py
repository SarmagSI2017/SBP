import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering as AHC
import scipy.cluster.hierarchy as sch

dataset = pd.read_csv('./datavclass.csv')
X = dataset.iloc[:, [1, 2]].values

#COMPLETE
#model = AHC(n_clusters=2, affinity='euclidean', linkage='complete')

#SINGLE
model = AHC(n_clusters=2, affinity='euclidean', linkage='single')

model.fit(X)

labels = model.labels_

plt.scatter(X[labels==0, 0], X[labels==0, 1], s=100, color='blue', label='1')
plt.scatter(X[labels==1, 0], X[labels==1, 1], s=100, color='red', label='2')

str = 'AHC - '+model.linkage
plt.title(str)
plt.legend(loc=2)
plt.show()