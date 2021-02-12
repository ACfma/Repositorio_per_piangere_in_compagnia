# -*- coding: utf-8 -*-
"""n_comp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hTw86Yka0a1q-jc9qZnTpcbPvsTeV3dY
"""

#from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


PERCENTAGE = [] #insert percentages found.
FEATURES = []

def n_comp(data, percentage):
    '''
    n_comp return the number of components respect to the percentage of cumulative/
    explained variance.

    Parameters
    ----------
    data : ndarray
        Array obtained from all images.
    percentage: float
        Percentage of cumulative explained variance.

    Returns
    -------
    Returns the number of PCs.

    '''
    pca = PCA(percentage)
    c_n = pca.n_components_
    return c_n
