# 28 - INSTALLING NUMPY IN PYCHARM

# install numpy package from pip
# go to command prompt and type "pip3 install numpy
# test at IDLE, type "import numpy"

# install numpy at PyCharm
# go to setting (ctrl + alt + s)
# click project : project name (YoutubeTelusko)
# click python interpreter
# click '+' icon, and search numpy
# click install package

from numpy import *

# with numpy, you can use multi dimensional array
arr = array([[4,6,8,4],[5,7,2,8]])
print(arr)
# you dont need to mention the type of array
arr2 = array([3,2,5,6])
print(arr2)
# but you can still mention the type
arr3 = array([3,2,5,6],int)
print(arr3)
