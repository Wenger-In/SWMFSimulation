from spacepy.pybats import IdlFile
import numpy as np
import matplotlib.pyplot as plt

# import data
data_path = 'E:/Research/Data/SWMF/output_0304/'
file_name = 'shl_mhd_3_n'
n_iter = 20000
file_str = file_name+str(int(n_iter)).zfill(8)
data_shl = IdlFile(data_path+'SC/'+file_str+'.out')

# grid
r = data_shl['r']
lon = np.array(data_shl['lon'])
lat = np.array(data_shl['lat'])
lonn,latt = np.meshgrid(lon,lat)

# extrace r_index: index 0 at 1 Rs
r_index = 0

# Alfven wave power density
I01 = np.array(data_shl['I01'])
I02 = np.array(data_shl['I02'])
w_pos = I01[r_index,::]
w_neg = I02[r_index,::]
Pa = (w_pos + w_neg)/2

# magnetic field
bx_arr = np.array(data_shl['Bx'])
by_arr = np.array(data_shl['By'])
bz_arr = np.array(data_shl['Bz'])
bx = bx_arr[r_index,::]
by = by_arr[r_index,::]
bz = bz_arr[r_index,::]
AbsB = np.sqrt(np.square(bx)+np.square(by)+np.square(bz))

# current density
jx_arr = np.array(data_shl['jx'])
jy_arr = np.array(data_shl['jy'])
jz_arr = np.array(data_shl['jz'])
jx = jx_arr[r_index,::]
jy = jy_arr[r_index,::]
jz = jz_arr[r_index,::]
AbsJ = np.sqrt(np.square(jx)+np.square(jy)+np.square(jz))

# plot figure
para_str = 'PA'

fig, ax = plt.subplots()
c = ax.pcolormesh(lonn,latt,Pa.T,cmap='jet')
fig.colorbar(c, ax=ax)
plt.title('(I01+I02)/2 [erg/cm3] (n'+str(int(n_iter)).zfill(8)+')')
plt.savefig(data_path+file_str+'_'+para_str+'.png')
plt.show()