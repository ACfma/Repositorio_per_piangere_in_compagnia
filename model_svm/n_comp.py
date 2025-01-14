"""n_comp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hTw86Yka0a1q-jc9qZnTpcbPvsTeV3dY
"""

from sklearn.decomposition import PCA


PERCENTAGE = []
FEATURES = []

def n_comp(data, percentage):
    '''
    n_comp return the number of components respect to the percentage of cumulative\
    explained variance.

    Parameters
    ----------
    data : array
        2D array obtained from all images.
    percentage: float
        Percentage of cumulative explained variance.

    Returns
    -------
    c_n : array
        Returns the number of PCs.

    '''
    pca = PCA(percentage)
    pca.fit_transform(data)
    c_n = pca.n_components_
    return c_n

