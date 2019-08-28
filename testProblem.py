# #from river_pollution import RiverPollution


# class Computer():
#     def __init__(self, computer, ram, ssd):
#         self.computer = computer
#         self.ram = ram
#         self.ssd = ssd

# class Laptop(Computer):
#     def __init__(self, computer, ram, ssd, model):
#         super().__init__(computer, ram, ssd)
#         self.model = model

# lenovo = Laptop('lenovo', 2, 512, 'l420')
# print('This computer is:', lenovo.computer)
# print('This computer has ram of', lenovo.ram)
# print('This computer has ssd of', lenovo.ssd)
# print('This computer has this model:', lenovo.model)



# Ask Question
# 74

# I researched first and couldn't find an answer to my question. I am trying to run multiple functions in parallel in Python.

# I have something like this:

# files.py

# import common #common is a util class that handles all the IO stuff

# dir1 = 'C:\folder1'
# dir2 = 'C:\folder2'
# filename = 'test.txt'
# addFiles = [25, 5, 15, 35, 45, 25, 5, 15, 35, 45]

# def func1():
#    c = common.Common()
#    for i in range(len(addFiles)):
#        c.createFiles(addFiles[i], filename, dir1)
#        c.getFiles(dir1)
#        time.sleep(10)
#        c.removeFiles(addFiles[i], dir1)
#        c.getFiles(dir1)

# def func2():
#    c = common.Common()
#    for i in range(len(addFiles)):
#        c.createFiles(addFiles[i], filename, dir2)
#        c.getFiles(dir2)
#        time.sleep(10)
#        c.removeFiles(addFiles[i], dir2)
#        c.getFiles(dir2)

# I want to call func1 and func2 and have them run at the same time. The functions do not interact with each other or on the same object. Right now I have to wait for func1 to finish before func2 to start. How do I do something like below:

# process.py

# from files import func1, func2

# runBothFunc(func1(), func2())

# I want to be able to create both directories pretty close to the same time because every min I am counting how many files are being created. If the directory isn't there it will throw off my timing.
# python
# shareedit
# edited Aug 26 '11 at 16:56
# asked Aug 26 '11 at 15:46
# lmcadory
# 5471514

# add a comment
# 5 Answers
# active
# oldest
# votes
# 115


# from multiprocessing import Process

# def func1():
#   print('func1: starting')
#   for i in range(10000000): pass
#   print('func1: finishing')

# def func2():
#   print( 'func2: starting')
#   for i in range(10000000): pass
#   print ('func2: finishing')

# if __name__ == '__main__':
#   p1 = Process(target=func1)
#   p1.start()
#   p2 = Process(target=func2)
#   p2.start()
#   p1.join()
#   p2.join()
# Import pandas 
import numpy as np
import pandas as pd


missing_values = ["n/a", "na", "--"]
# Read in white wine data 
white =pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';', na_values=missing_values)

# Read in red wine data 
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';', na_values=missing_values)

wbcd = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data", sep=';', na_values=missing_values)


df = pd.DataFrame([[1,2],[4,2],[np.nan,8]], index= ['esi', 'mohsen', 'aboo'], columns = ['chert','yugi'])
F = pd.DataFrame([[2,3,5,5],[5,4,6,7],[5,4,6,7], [4,7,2,1], [4,5,6,9],[np.nan,6,7,np.nan],[1,2,9,np.nan], [5,8,7,np.nan]], index=['mohsen','naji','ali','baba', 'maman','panje','rasoli','eshghan'], columns=['khobi','paki','refaghat','sedaghat'])

data = pd.read_csv("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv")
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data")
cx=0

import sys
from impyute.imputation.cs import fast_knn, mice
from sklearn import datasets, linear_model
from sklearn.model_selection import KFold

diabetes=datasets.load_diabetes()
df = pd.DataFrame(diabetes.data)
y=diabetes.target
iris=datasets.load_iris()
df1=pd.DataFrame(iris.data)
x=iris.target
vc=0