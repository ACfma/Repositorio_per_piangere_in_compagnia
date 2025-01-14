# -*- coding: utf-8 -*-
"""
Example of tool used to compare MMSE from AD_CTRL metadata to CNN prediction
in model_cnn.ipynb.

"""
import argparse
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.stats import spearmanr

def plot_mmse_prediction(table, test_names, classifier, test_x):
    '''
    Helps to understand how to convert names in the table df with those
    of the split "test_names" list in order to take MMSE and compares them.

    Parameters
    ----------
    test_names : list
        list with test names.
    X : array
        Array of test data.
    classifier : tensorflow.python.keras.\
            engine.Model
        Model, Convolutional NN.

    Returns
    -------
    spr_rank : scipy.stats.stats.SpearmanrResult
        Sperman Rank.

    '''
    csv_table = pd.read_table(table)
    mmse = []
    data = []
    for j in test_names:
        for i,k in enumerate(csv_table['ID'].values):
            if k + '.' in j:
                mmse.append(csv_table['MMSE'].values[i])
                if 'AD' in k:
                    data.append(True)
                else:
                    data.append(False)

    data = np.array(data)
    mmse = np.array(mmse)
    prediction = classifier.predict(test_x)
    plt.figure()
    plt.scatter(mmse[data == True], prediction[data == True],\
                facecolors='none', edgecolors='g')
    plt.scatter(mmse[data == False], prediction[data == False],\
                facecolors='none', edgecolors='b')
    plt.xlabel('MMSE')
    plt.ylabel('Model predict')
    plt.title('Distribution of subject')
    plt.legend(['AD', 'CTRL'],loc="upper left")
    plt.grid()

    spr_rank = spearmanr(mmse,prediction)
    return spr_rank

if __name__ == "__main__":
    # Arguments
    parser = argparse.ArgumentParser(description="Tool to create the model\
                                     and train the dataset")
    parser.add_argument('-table', help='Path to your metadata.csv table', type=str)
    args = parser.parse_args()
    df_table = args.table
