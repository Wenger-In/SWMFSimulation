from spacepy.pybats import IdlFile
from spacepy.pybats.bats import MagGridFile, Bats2d
import numpy as np
import matplotlib.pyplot as plt

## read .outs file from SWMF
data = IdlFile('E:/Research/Data/SWMF/output_1004/z=0_var_2_n00000000_00060000.outs')

# # plot the index order of grids 
# plt.scatter(data['y'], data['z'], c=np.linspace(0, 512, len(data['y'])))
# plt.axis('equal')
# plt.show()

## plot the profile in Y-Z plane
fig, ax = plt.subplots()
# tpc = ax.tripcolor(data['y'], data['z'], np.log10(np.sqrt(np.square(data['bx'])+np.square(data['by'])+np.square(data['bz']))))
tpc = ax.tripcolor(data['x'], data['y'], np.log10(np.sqrt(np.square(data['bx'])+np.square(data['by'])+np.square(data['bz']))))
# tpc = ax.tripcolor(data['y'], data['z'], np.log10(np.abs(data['bz'])))

# # mark the bad point with non-integer of 'status'
# tpc = ax.tripcolor(data['y'], data['z'], data['status'])
# dy = data['y']
# dz = data['z']
# dstatus = data['status']
# ax.plot(dy[233], dz[233], 'o', markersize=2, color='grey')
# ax.plot(dy[260], dz[260], 'o', markersize=2, color='grey')
# ax.plot(dy[290], dz[290], 'o', markersize=2, color='grey')

fig.colorbar(tpc)
plt.axis('equal')
plt.title('log10|B| in Y-Z plane')
# plt.title('log10|Bz| in Y-Z plane')
plt.xlabel('Y [Rs]')
plt.ylabel('Z [Rs]')
plt.show()

# dstatus = data['status']