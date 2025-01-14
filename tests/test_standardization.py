# -*- coding: utf-8 -*-
"""Test_Standardization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-U_gO4365PQg0VlQHQZWmAAvIlDtqVwQ
"""

import unittest
import os
#import sklearn
import numpy as np
from sklearn.preprocessing import StandardScaler
import SimpleITK as sitk
import glob


PATH = os.path.abspath('')
FILE = '/tests/smwc1CTRL-1.nii'
FILE = PATH+FILE

img = sitk.ReadImage(FILE, imageIO = "NiftiImageIO")
img_a = sitk.GetArrayFromImage(img[:, 40, :])

import unittest
class StandardTest(unittest.TestCase):

 def test_st(self):
    self.X = img_a
    self.stand_data = StandardScaler().fit_transform(self.X)

    var_s = np.var((self.X - self.X.mean())/self.X.std())

    np.testing.assert_array_almost_equal(np.var(self.stand_data), var_s, decimal=1)


if __name__=='__main__':
    unittest.main()
