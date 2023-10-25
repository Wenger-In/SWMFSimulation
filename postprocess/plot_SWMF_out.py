from spacepy.pybats import IdlFile
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import pyvista
import pandas as pd

#################### if the output file is '3d ful' ####################
# data_path = 'E:/Research/Data/SWMF/output_1005/'
# file_name = '3d__ful_3_n'
# n_iter = 60000
# file_str = file_name+str(int(n_iter)).zfill(8)
# data_3d=IdlFile(data_path+'SC/'+file_str+'.out')

# xg_arr = np.array(data_3d['x'])
# yg_arr = np.array(data_3d['y'])
# zg_arr = np.array(data_3d['z'])
# bx_arr = np.array(data_3d['Bx'])
# by_arr = np.array(data_3d['By'])
# bz_arr = np.array(data_3d['Bz'])

# br_arr = bz_arr
# for ig in range(len(xg_arr)):
#     r_vec = [xg_arr[ig], yg_arr[ig], zg_arr[ig]]
#     b_vec = [bx_arr[ig], by_arr[ig], bz_arr[ig]]
#     br_arr[ig] = np.dot(r_vec,b_vec) / np.sqrt(np.dot(r_vec,r_vec))

# mesh_g = pyvista.StructuredGrid(xg_arr, yg_arr, zg_arr)
# mesh_g.point_data['values'] = br_arr.ravel(order='F')  # also the active scalars
# isos_b0 = mesh_g.contour(isosurfaces=1, rng=[0, 0])
# isos_b0.plot(opacity=0.8)
################################################################################

#################### if the output file is '2d cut' ####################
# data_path = 'E:/Research/Data/SWMF/output_1008/'
# file_name = '2d__mhd_4_n'
# n_iters = np.linspace(300,39000,130)
# # n_iters = [300,9900,10200,39000]

# # para_str = 'rho'
# # para_str = 'Bz'
# # para_str = 'B'
# para_str = 'V'

# frames=[]
# for n_iter in n_iters:
#     file_str = file_name+str(int(n_iter)).zfill(8)
#     data_2d=IdlFile(data_path+'SC/'+file_str+'.out')
#     fig, ax = plt.subplots()

#     # tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.log10(np.array(data_2d[para_str])))
#     # tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.array(data_2d[para_str]))
#     # tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.log10(np.sqrt(np.square(np.array(data_2d['Bx']))+np.square(np.array(data_2d['By']))+np.square(np.array(data_2d['Bz'])))))
#     tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.sqrt(np.square(np.array(data_2d['Ux']))+np.square(np.array(data_2d['Uy']))+np.square(np.array(data_2d['Uz']))))
    
#     # plt.title('log10 Rho [log(g/cm^3)]'+'(n'+str(int(n_iter)).zfill(8)+')')
#     # plt.title('Bz [G]'+'(n'+str(int(n_iter)).zfill(8)+')')
#     # plt.title('log10 |B| [log10(G)]'+'(n'+str(int(n_iter)).zfill(8)+')')
#     plt.title('|V| [km/s]'+'(n'+str(int(n_iter)).zfill(8)+')')
    
#     plt.colorbar(tpc)
    
#     # tpc.set_clim(-21.2,-18.7)
#     # tpc.set_clim(-2e-4,4e-4)
#     # tpc.set_clim(0,-4)
#     tpc.set_clim(0,450)

#     plt.axis('equal')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.savefig(data_path+file_str+'_'+para_str+'.png')
#     plt.close()
#     # plt.show()
#     frames.append(imageio.imread(data_path+file_str+'_'+para_str+'.png'))
# imageio.mimsave(data_path+file_str+'_'+para_str+'.mp4',frames,fps=8)
# quit()
################################################################################

#################### if the output file is 'z=0 var' ####################
# data_path = 'E:/Research/Data/SWMF/output_0126/'
# file_name = 'z=0_var_2_n'
# n_iters = np.append(np.linspace(200,6000,30), np.linspace(6050,6650,13))
# # n_iters = [100,200,300,400,500,600,700,800]

# # para_str = 'rho'
# para_str = 'bz'
# # para_str = 'B'
# # para_str = 'V'

# frames=[]
# for n_iter in n_iters:
#     file_str = file_name+str(int(n_iter)).zfill(8)
#     data_2d=IdlFile(data_path+'SC/'+file_str+'.out')
#     fig, ax = plt.subplots()
    
#     # tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.log10(np.array(data_2d[para_str])))
#     tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.array(data_2d[para_str]))
#     # tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.log10(np.sqrt(np.square(np.array(data_2d['bx']))+np.square(np.array(data_2d['by']))+np.square(np.array(data_2d['bz'])))))
#     # tpc=ax.tripcolor(data_2d['x'], data_2d['y'], np.sqrt(np.square(np.array(data_2d['ux']))+np.square(np.array(data_2d['uy']))+np.square(np.array(data_2d['uz']))))
    
#     # plt.title('log10 Rho [log(g/cm^3)]'+'(n'+str(int(n_iter)).zfill(8)+')')
#     plt.title('Bz [G]'+'(n'+str(int(n_iter)).zfill(8)+')')
#     # plt.title('log10 |B| [log10(G)]'+'(n'+str(int(n_iter)).zfill(8)+')')
#     # plt.title('|V| [km/s]'+'(n'+str(int(n_iter)).zfill(8)+')')
    
#     plt.colorbar(tpc)
    
#     # tpc.set_clim(-21.2,-18.7)
#     tpc.set_clim(-6e-4,4e-4)
#     # tpc.set_clim(0,-4)
#     # tpc.set_clim(0,450)
    
#     plt.axis('equal')
#     plt.xlim(-23, 23)
#     plt.ylim(-23, 23)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.savefig(data_path+file_str+'_'+para_str+'.png')
#     plt.close()
#     # plt.show()
#     frames.append(imageio.imread(data_path+file_str+'_'+para_str+'.png'))
# imageio.mimsave(data_path+file_str+'_'+para_str+'.mp4',frames,fps=2)
# quit()
################################################################################

#################### if the output file is 'x=0 var' ####################
data_path = 'E:/Research/Data/SWMF/output_0304/'
file_name = 'x=0_var_1_n'
# n_iters = np.append(np.linspace(0,56000,15), np.linspace(56050,56300,6))
n_iters = [20000]

# para_str = 'rho'
para_str = 'B'
# para_str = 'V'
# para_str = 'br'

frames=[]
for n_iter in n_iters:
    file_str = file_name+str(int(n_iter)).zfill(8)
    data_2d=IdlFile(data_path+'SC/'+file_str+'.out')
    
    fig, ax = plt.subplots()
    
    # xg_arr = np.array(data_2d['x'])
    yg_arr = np.array(data_2d['y'])
    zg_arr = np.array(data_2d['z'])
    bx_arr = np.array(data_2d['bx'])
    by_arr = np.array(data_2d['by'])
    bz_arr = np.array(data_2d['bz'])

    br_arr = bz_arr
    for ig in range(len(yg_arr)):
        r_vec = [0, yg_arr[ig], zg_arr[ig]]
        b_vec = [bx_arr[ig], by_arr[ig], bz_arr[ig]]
        br_arr[ig] = np.dot(r_vec,b_vec) / np.sqrt(np.dot(r_vec,r_vec))
    
    # tpc=ax.tripcolor(data_2d['y'], data_2d['z'], np.log10(np.array(data_2d[para_str])))
    tpc=ax.tripcolor(data_2d['y'], data_2d['z'], np.log10(np.sqrt(np.square(np.array(data_2d['bx']))+np.square(np.array(data_2d['by']))+np.square(np.array(data_2d['bz'])))))
    # tpc=ax.tripcolor(data_2d['y'], data_2d['z'], np.sqrt(np.square(np.array(data_2d['ux']))+np.square(np.array(data_2d['uy']))+np.square(np.array(data_2d['uz']))))
    # tpc=ax.tripcolor(data_2d['y'], data_2d['z'], np.log10(abs(br_arr)))
    # tpc=ax.tripcolor(data_2d['y'], data_2d['z'], br_arr)
    
    # plt.title('log10 Rho [log(g/cm^3)]'+'(n'+str(int(n_iter)).zfill(8)+')')
    plt.title('log10 |B| [log10(G)]'+'(n'+str(int(n_iter)).zfill(8)+')')
    # plt.title('|V| [km/s]'+'(n'+str(int(n_iter)).zfill(8)+')')
    # plt.title('log10 |br| [log10(G)]'+'(n'+str(int(n_iter)).zfill(8)+')')
    # plt.title('br [G]'+'(n'+str(int(n_iter)).zfill(8)+')')
    
    plt.colorbar(tpc)
    
    # tpc.set_clim(-21.5,-18.5)
    tpc.set_clim(-4,0)
    # tpc.set_clim(100,800)
    # tpc.set_clim(-6,0)
    # tpc.set_clim(-0.01,0.01)
    
    plt.axis('equal')
    plt.xlim(-23, 23)
    plt.ylim(-23, 23)
    plt.xlabel('y')
    plt.ylabel('z')
    plt.savefig(data_path+file_str+'_'+para_str+'.png')
    plt.close()
    # plt.show()
    frames.append(imageio.imread(data_path+file_str+'_'+para_str+'.png'))
imageio.mimsave(data_path+file_str+'_'+para_str+'.mp4',frames,fps=2)
quit()
################################################################################

#################### if the output file is 'box MHD' ####################
# data_path = 'E:/Research/Data/SWMF/output_1014/'
# file_name = 'box_mhd_5_n'
# n_iter = 3000
# file_str = file_name+str(int(n_iter)).zfill(8)
# data_3d=IdlFile(data_path+'SC/'+file_str+'.out')

# xg_arr, yg_arr, zg_arr = np.meshgrid(np.array(data_3d['y']),np.array(data_3d['x']),np.array(data_3d['z']))
# bx_arr = np.array(data_3d['Bx'])
# by_arr = np.array(data_3d['By'])
# bz_arr = np.array(data_3d['Bz'])

# br_arr = bz_arr
# for ig in range(len(np.array(data_3d['x']))):
#     for jg in range(len(np.array(data_3d['y']))):
#         for kg in range(len(np.array(data_3d['z']))):
#             r_vec = [xg_arr[ig,jg,kg], yg_arr[ig,jg,kg], zg_arr[ig,jg,kg]]
#             b_vec = [bx_arr[ig,jg,kg], by_arr[ig,jg,kg], bz_arr[ig,jg,kg]]
#             br_arr[ig,jg,kg] = np.dot(r_vec,b_vec) / np.sqrt(np.dot(r_vec,r_vec))

# mesh_g = pyvista.StructuredGrid(xg_arr, yg_arr, zg_arr)
# mesh_g.point_data['values'] = br_arr.ravel(order='F')  # also the active scalars
# isos_b0 = mesh_g.contour(isosurfaces=1, rng=[0, 0])
# isos_b0.plot(opacity=0.8)
################################################################################

#################### if the output file is 'field 2d' ####################
# data_path = 'E:/Research/Data/SWMF/magnetogram/FDIPS/FDIPS1206/'
# file_name = 'field_2d'

# data_2d=IdlFile(data_path+file_name+'.out')
# fig, ax = plt.subplots()

# x = np.linspace(0,data_2d['grid'][0],data_2d['grid'][0])
# y = np.linspace(-90,data_2d['grid'][1]-90,data_2d['grid'][1])
# xx,yy = np.meshgrid(x,y)

# tpc = ax.pcolormesh(xx, yy, np.array(data_2d['Br']).T, cmap='RdBu')
# plt.colorbar(tpc)
# tpc.set_clim(-50,50)

# plt.title('Magnetogram based on FDIPS')

# plt.axis('equal')
# plt.xlim((0,360))
# plt.ylim((-90,90))
# plt.xlabel('longitude')
# plt.ylabel('latitude')
# plt.savefig(data_path+'1.png')
# plt.show()

# dataframe = pd.DataFrame(np.array(data_2d['Br']).T)
# dataframe.to_csv(data_path+'Br.csv',index=False,sep=',')
################################################################################
