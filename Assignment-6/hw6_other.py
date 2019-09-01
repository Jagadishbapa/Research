import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import mixture
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.metrics.cluster import adjusted_mutual_info_score


# Task [3]: cluster instances and visualize them in 2D space 
# --------------------------------------------------------------------------
# !! for different methods, you need to import different scikit learn libraries !!
# the template only includes one example library 
# search scikit-learn homepage to find out more libraries 
# --------------------------------------------------------------------------


# step 1. loda data 
# no need to split it; we will cluster all examples 
data = np.genfromtxt('crimecommunity.csv', delimiter=',')
sample = data[:,0:-2]
label_desired = data[:,-2]


# -----------------------------------------------------------------------------------
# experiment 1: K-means Clustering
# -----------------------------------------------------------------------------------
# first, construct a Kmeans model using function "KMeans"
# find optimal hyperpameter n_clusters in {1, 2, 3, 5, 10}
model_kmeans = KMeans(n_clusters=3)
# then, fit the model using sample using function "fit"
# finally, evaluate the model the sample  
# first get the clustering result 
label_cluster_kmeans = model_kmeans.fit(sample).predict(sample)
# here, we assume desired clustering label is given and compare our clustering 
# result with the desired one using function "adjusted_mutual_info_score"
# higher MI suggests higher clustering quality 
MI_kmeans = adjusted_mutual_info_score(label_desired, label_cluster_kmeans)
print(MI_kmeans)


# -----------------------------------------------------------------------------------
# experiment 2: Gaussian-Mixture Model (GMM) Clustering
# -----------------------------------------------------------------------------------
# first, construct a GMM model using function "GaussianMixture"
# find optimal hyperpameter n_components in {1, 2, 3, 5, 10}
model_gmm = mixture.GaussianMixture(n_components = 2)
# fit the model
# evaluate the model 
label_cluster_gmm = model_gmm.fit(sample).predict(sample)
MI_gmm = adjusted_mutual_info_score(label_desired, label_cluster_gmm)
print(MI_gmm)


# -----------------------------------------------------------------------------------
# experiment 3: Principal Component Analysis (PCA) for dimension reduction 
# -----------------------------------------------------------------------------------
# now you want to visualize the clustering result in a two-dimensional feature space 
# you can apply PCA to reduce the dimension of the original space to 2
# ------- 
# first, construct a PCA model using function "PCA"
# set hyper-parameter n_components=2 (as we only need two dimensions for visualization here)
model_pca = PCA(n_components = 2).fit(sample)
# fit the model on sample 
#model_pca.fit(sample)
# apply model to reduce dimension using function "transform"
sample_pca = model_pca.transform(sample)

# now, plot your data distribution based on sample_pca
# you can plot examples assigned to different clusters (by Kmeans) using different colors 
index_set = np.unique(label_cluster_kmeans)
index_size = len(index_set)
cmap = mpl.cm.autumn
for i in index_set:
    index_i= np.where(label_cluster_kmeans==i)[0]
    plt.plot(sample_pca[index_i,0],sample_pca[index_i,1],'o',color = cmap(i/index_size))
plt.show()
# you can also reconstruct sample_pca in the original space using function "inverse_transform" 
sample_reconstruct = model_pca.inverse_transform(sample_pca)
# now you measure reconstruction error, averaged over all examples
loss = np.sum((sample_reconstruct - sample)**2,axis=1)
print(np.mean(loss))




