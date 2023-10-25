from spacepy.pybats import IdlFile
import numpy as np
import matplotlib.pyplot as plt
from os.path import exists
from urllib.request import urlretrieve
import swmfio as swmfio

urlbase = 'http://mag.gmu.edu/git-data/swmfio/3d__var_2_e20190902-041000-000'
# filebase = swmfio.dlfile(urlbase, progress=True)
# filebase = 'E:\\Research\\Data\\SWMF\\output_1005\\SC\\60000\\3d__ful_3_n00060000'
filebase = 'C:\\Users\\rzhuo\\AppData\\Local\\Temp\\mag.gmu.edu/git-data/swmfio\\3d__var_2_e20190902-041000-000'

print("Reading and creating native grid interpolator" + filebase + ".{tree, info, out}")
batsclass = swmfio.read_batsrus(filebase)
# Time: 0:00:01.856912

assert batsclass.data_arr.shape == (5896192, 19)

# Get a 513th value of x, y, z, and rho
var_dict = dict(batsclass.varidx)
rho = batsclass.data_arr[:, var_dict['rho']][513]
x = batsclass.data_arr[:,var_dict['x']][513]
y = batsclass.data_arr[:,var_dict['y']][513]
z = batsclass.data_arr[:,var_dict['z']][513]
print(x, y, z, rho)
# -71.25 -15.75 -7.75 4.22874
