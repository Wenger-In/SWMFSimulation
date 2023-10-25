from spacepy.pybats import IdlFile
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import pyvista

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

# Alfven wave power density
I01 = np.array(data_shl['I01'])
I02 = np.array(data_shl['I02'])
Pe = np.array(data_shl['Pe'])
P = np.array(data_shl['P'])

# extrace r_index: 0-13 (1-8 Rs)
r_index = 8
r_index_str = '8'
# rho = np.array()
w_pos = I01[r_index,::]
w_neg = I02[r_index,::]
Pa = (w_pos + w_neg)/2
# Pa = Pe[1,::]
# Pa = P[1,::]

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
# para_str = 'PA'
para_str = 'J'
# para_str = 'B'

lonn,latt = np.meshgrid(lon,lat)
fig, ax = plt.subplots()

# c = ax.pcolormesh(lonn,latt,Pa.T,cmap='jet')
c = ax.pcolormesh(lonn,latt,np.log10(AbsJ).T,cmap='jet')
# c = ax.pcolormesh(lonn,latt,np.log10(AbsB).T,cmap='jet')

fig.colorbar(c, ax=ax)

# plt.title('(I01+I02)/2 [erg/cm3] (n'+str(int(n_iter)).zfill(8)+')')
plt.title('log10 |J| [log10(uA/m2)] (n'+str(int(n_iter)).zfill(8)+')')
# plt.title('log10 |B| [log10(G)] (n'+str(int(n_iter)).zfill(8)+')')

plt.savefig(data_path+para_str+'_'+file_str+'_'+r_index_str+'.png')
plt.show()