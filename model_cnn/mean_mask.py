# -*- coding: utf-8 -*-
"""
Module to obatain a mean mask from an array of simpleITK images.
"""
import os
import glob
import argparse
import numpy as np
import SimpleITK as sitk

def mean_mask(images, ctrl, overlap = 0.97):
    '''
    mean_mask creates a mean mask based on a threshold along all the images\
     given as input in order to retain just the most important voxels selected\
     in "Automatic" or "Manual" mode.

    Parameters
    ----------
    images : list or nd array of SimpleITK.Image
        List of images to be confronted in order to obtain a mean mask.

    ctrl : int
        Number of control subject.

    overlap : float
        Percentage of overlapping between all the images masks. overlap = 1\
         for taking into account all the feature selected by the single masks.\
        Must be a float between 0 and 1.
    Returns
    -------
    m_mean : ndarray
        Array of the same dimension of a single input image.

    '''

    def filter_gm(image):
        '''
        filter_gm uses RenyiEntropyThresholdImageFilter in order to create an\
         ndarray.

        Parameters
        ----------
        image : SimpleITK.Image
            Image to apply the filter to.

        Returns
        -------
        None.

        '''
        nonlocal masks
        threshold_filters= sitk.RenyiEntropyThresholdImageFilter() # best threshold i could find
        threshold_filters.SetInsideValue(0)#
        threshold_filters.SetOutsideValue(1)#binomial I/O
        thresh_img = threshold_filters.Execute(image)
        msk = sitk.GetArrayFromImage(thresh_img)
        masks.append(msk)

    a_m = ''

    while a_m != 'Automatic' and a_m != 'Manual':
        a_m = input("\nWhat kind of filter do you want to apply?\
                    \n-Type 'Automatic' if you like to use an automatic filter\
                    \n-Type 'Manual' for select your threshold.\n")

    masks = []

    if a_m == "Automatic":
        for item in images:
            filter_gm(item)

    if a_m == "Manual":
        thr = float(input("Insert your threshold:"))
        for item in images:
            masks.append(
                np.where(sitk.GetArrayFromImage(item)>thr,1,0))
    #Building an histogram of occourrences of brain segmentation
    m_sum = np.sum(np.array(masks),
                   axis = 0)
    #Alzheimer desease is diagnosticated by a loss of GM in some areas
    m_up = np.where(m_sum>(1-overlap)*ctrl,
                    m_sum, 0)
    #creating mean mask of ints
    m_mean = np.where(m_up > 0, 1, 0)

    return m_mean

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to create mean mask of images")
    parser.add_argument('-path', help='Path to your files', type=str)
    args = parser.parse_args()
    path = args.path
    FILES = r"\*.nii" #find all nifti files with .nii in the name
    path = path + FILES
    subj = glob.glob(os.path.normpath(path), recursive=True)
    img = [sitk.ReadImage(subj[0], imageIO = "NiftiImageIO")]
    mask = mean_mask(img,1)