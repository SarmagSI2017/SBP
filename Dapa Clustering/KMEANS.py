import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

dataset = pd.read_csv('./datavclass.csv')
X = dataset.iloc[:, [1, 2]].values

kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)
labels = kmeans.fit_predict(X)

plt.scatter(X[labels==0, 0], X[labels==0, 1], s=100, color='blue', label='1')
plt.scatter(X[labels==1, 0], X[labels==1, 1], s=100, color='red', label='2')

plt.title('K-MEANS')
plt.legend(loc=2)
plt.show()