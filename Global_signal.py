import numpy as np
import os
import glob
import matplotlib.colors as colors
from numpy import linspace
import matplotlib.colorbar
from matplotlib import ticker
import matplotlib.pyplot as plt

data_1 = np.loadtxt('Programs/Power_k0.1_fid')
data_2 = np.loadtxt('Programs/Power_k0.1_updated_2')
#data_3 = np.loadtxt('Programs/Power_k0.1')
plt.plot(data_1[:,0], data_1[:,2], label  =r"${\rm constant\ Lx/SFR}$", c = 'k')
plt.plot(data_2[:,0], data_2[:,2], label  =r"${\rm Lx/SFR\ Fraogs}$", c = 'b')

#plt.plot(data_3[:,0], data_3[:,2], label  =r"${\rm Lx/SFR\ Fragos_2}$", c = 'r')
plt.xlabel(r"${{\rm Redshift},\,z}$",fontsize='large')
plt.ylabel(r"${\overline{\delta T}^{2}_{\rm b}\Delta^{2}_{21}\,\,[\rm mK^{2}]}$",fontsize='large')
plt.legend()
plt.close()
#plt.savefig("Global_signal.pdf")

z_187 = np.loadtxt('z_187')[:-1]
def PS_file(z):
    
    desired_file = 0
    
    for filename in glob.iglob('/home/hkaur/storage2/Xrayproject/21cmFAST/Output_files/Deldel_T_power_spec/ps_z*'): 
        if 'z%06.2f'%z  in filename:
            desired_file = filename
    return desired_file

def PS_file_updated(z):

    desired_file = 0
    
    for filename in glob.iglob('/home/hkaur/COMP167/21cmFAST/Output_files_updated_2/Deldel_T_power_spec_updated_2/ps_z*'): 
        if 'z%06.2f'%z  in filename:
            desired_file = filename
    return desired_file

k_list = np.log10(np.loadtxt(PS_file(6.0))[:,0])
matrix = np.zeros((11,75))
def PS_matrix(k):
    PS_list_all_z = []
    for i,z in enumerate(z_187) :
        data = np.loadtxt(PS_file(z))
        PS_list = data[:,1]
        PS_list_all_z.append(PS_list)
    for i in range(75):
        list_i = PS_list_all_z[i]
        for p,j in enumerate(list_i):
            matrix[p,i] = j
    return matrix
def PS_matrix_updated(k):
    PS_list_all_z = []
    for i,z in enumerate(z_187) :
        data = np.loadtxt(PS_file_updated(z))
        PS_list = data[:,1]
        PS_list_all_z.append(PS_list)
    for i in range(75):
        list_i = PS_list_all_z[i]
        for p,j in enumerate(list_i):
            matrix[p,i] = j
    return matrix


plt.plot(z_187, PS_matrix(0)[2,:], label  =r"${\rm constant\ Lx/SFR}$", c = 'k')
plt.plot(z_187, PS_matrix_updated(0)[2,:], label  =r"${\rm Fragos\ Lx/SFR}$", c = 'b')
plt.xlabel(r"${{\rm Redshift},\,z}$",fontsize='large')
plt.ylabel('$\delta T_{b}^{2}\Delta_{21}^{2}$ $[$mk$^{2}]$',fontsize='large')
plt.text(20,10, r'${\rm k = 0.1\mathrm{Mpc^{-1}}}$', fontsize=14)
plt.legend()
plt.show()
#plt.savefig("Power_spec_k_0_6.pdf")
