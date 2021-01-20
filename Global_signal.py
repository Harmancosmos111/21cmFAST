import numpy as np
import os
import glob
import matplotlib.colors as colors
from numpy import linspace
import matplotlib.colorbar
from matplotlib import ticker
import matplotlib.pyplot as plt

data_1 = np.loadtxt('Programs/Power_k0.1_updated_2')
#data_2 = np.loadtxt('Programs/Power_k0.1')
data_4 = np.loadtxt('Programs/Power_k0.1_38')
data_5 = np.loadtxt('Programs/Power_k0.1_39.5')
data_6 = np.loadtxt('Programs/Power_k0.1_5.39.5')
data_7 = np.loadtxt('Programs/Power_k0.1_8e40')
data_8 = np.loadtxt('Programs/Power_k0.1_3e39.5')
data_3 = np.loadtxt('Programs/Power_k0.1_fid')
plt.plot(data_1[:,0], data_1[:,2], label  =r"${\rm Lx/SFR\ Fraogs}$", c = 'r')
#plt.plot(data_2[:,0], data_2[:,2], label  =r"${\rm Lx/SFR\ Fraogs2}$", c = 'b')
plt.plot(data_8[:,0], data_8[:,2], c = 'g',label  =r"${\rm Lx/SFR\ = 3e39.5}$")
plt.plot(data_7[:,0], data_7[:,2], c = 'c', label  =r"${\rm Lx/SFR\ = 8e40}$")
plt.plot(data_6[:,0], data_6[:,2], c = 'b',label  =r"${\rm Lx/SFR\ = 5e39.5}$")
plt.plot(data_5[:,0], data_5[:,2], c = 'm',label  =r"${\rm Lx/SFR\ = 1e39.5}$")
plt.plot(data_4[:,0], data_4[:,2], c = 'y',label  =r"${\rm Lx/SFR\ = 1e38}$")
plt.plot(data_3[:,0], data_3[:,2], label  =r"${\rm Fiducial\ Lx/SFR\ = 1e40.5}$", c = 'k')
plt.xlim(6,20)
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

def PS_file_Fragos(z):

    desired_file = 0
    
    for filename in glob.iglob('/home/hkaur/COMP167/21cmFAST/Output_files_updated/Deldel_T_power_spec/ps_z*'): 
        if 'z%06.2f'%z  in filename:
            desired_file = filename
    return desired_file

def PS_file_myattempt(z):

    desired_file = 0

    for filename in glob.iglob('/home/hkaur/COMP167/21cmFAST/Output_files/Deldel_T_power_spec/ps_z*'):  
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
def PS_matrix_Fragos(k):
    PS_list_all_z = []
    for i,z in enumerate(z_187) :
        data = np.loadtxt(PS_file_Fragos(z))
        PS_list = data[:,1]
        PS_list_all_z.append(PS_list)
    for i in range(75):
        list_i = PS_list_all_z[i]
        for p,j in enumerate(list_i):
            matrix[p,i] = j
    return matrix
def PS_matrix_myattempt(k):
    PS_list_all_z = []
    for i,z in enumerate(z_187) :
        data = np.loadtxt(PS_file_myattempt(z))
        PS_list = data[:,1]
        PS_list_all_z.append(PS_list)
    for i in range(75):
        list_i = PS_list_all_z[i]
        for p,j in enumerate(list_i):
            matrix[p,i] = j
    return matrix


plt.plot(z_187, PS_matrix(0)[6,:], label  =r"${\rm Fiducial\ Lx/SFR\ = 1e40.5}$", c = 'k')
plt.plot(z_187, PS_matrix_Fragos(0)[6,:], label  =r"${\rm Fragos\ Lx/SFR}$", c = 'r')
plt.plot(z_187, PS_matrix_myattempt(0)[6,:], label  =r"${\rm Lx/SFR\ = 1e39.5}$", c = 'g')
plt.xlabel(r"${{\rm Redshift},\,z}$",fontsize='large')
plt.ylabel('$\delta T_{b}^{2}\Delta_{21}^{2}$ $[$mk$^{2}]$',fontsize='large')
plt.text(20,10, r'${\rm k = 0.6\mathrm{Mpc^{-1}}}$', fontsize=14)
plt.legend()
plt.show()
#plt.savefig("Power_spec_k_0_6.pdf")
