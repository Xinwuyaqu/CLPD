#!usr/bin/python

import xlrd
import xlwt
import numpy  as np
import pandas as pd
from numpy import mat

import functions
from functions import *

file_name = '/result'

nodes=[1]
node = nodes[0]

programs = [[20,-1],[22,260],[280,445],[460,1440],[1485,1690],[1705,1879]]
programName=['All','RandomAccess','PTRANS','DGEMM','STREAM','FFT']
selectProgram=0
FilterSize=10

start_local = programs[selectProgram][0]
suit_len = programs[selectProgram][1]
#start_local = 1
#suit_len = -1
wb = xlrd.open_workbook('./' + str(node) + file_name + '.xlsx')
sheet=wb.sheet_by_index(0)
cpu_power=Filter(sheet.col_values(1)[start_local:suit_len],FilterSize) #pkg_power
mem_power=Filter(sheet.col_values(2)[start_local:suit_len],FilterSize) #dram_power
sys_power=[p+q+20 for p,q in zip(cpu_power,mem_power)]  #total power

#sys_power=[p+q for p,q in zip(cpu_power, mem_power)]

#CPU group
cas_count_read1 = Filter(sheet.col_values(21)[start_local:suit_len],FilterSize)
clockticks1     = Filter(sheet.col_values(23)[start_local:suit_len],FilterSize)
L1_dmisses      = Filter(sheet.col_values(32)[start_local:suit_len],FilterSize)
cpu_cycles      = Filter(sheet.col_values( 9)[start_local:suit_len],FilterSize)

#MEM group
branch_loads    = Filter(sheet.col_values(41)[start_local:suit_len],FilterSize)
cache_misses    = Filter(sheet.col_values( 7)[start_local:suit_len],FilterSize)

print(sheet.col_values(21)[0])
print(sheet.col_values(23)[0])
print(sheet.col_values(32)[0])
print(sheet.col_values(9)[0])
print(sheet.col_values(41)[0])
print(sheet.col_values(7)[0])

print('====================== 导入数据量为 ===============================')
statslen = len(cpu_power)
print(statslen)
print('======================= 初始化系数 ================================')

ccr1 = Normalize(cas_count_read1) # +
ctk1 = [i for i in Normalize(clockticks1)]     # -
ldm1 = Normalize(L1_dmisses)      # +
ccls = [i for i in Normalize(cpu_cycles)]      # -


blds = [i for i in Normalize(branch_loads)]    # -
cmis = Normalize(cache_misses)    # +
'''
mem_used = [(1-i/6.5e10)*10 for i in free]
mem_l2ms = [(p+q)/6e8 for p,q in zip(llc_ldmis,llc_stmis)]

cpu_used = [(100-i)/10 for i in idle]
cpu_int = [i/25000 for i in sys_int]
cpu_run = [i/20 for i in run]
cpu_csw = [i/2000 for i in csw]
'''
state_group = [ccr1, ctk1, ldm1, ccls, blds, cmis]
state_num = len(state_group)+1

initialStart = 0
initialEnd = 0

if statslen < initialEnd:
    print('数据量过少！')
    exit()

initial_group = [g[initialStart:initialEnd] for g in state_group]
initial_power = sys_power[initialStart:initialEnd]
w = GetCoefficient(initial_group, initial_power)
w = GetCoefficient(state_group, sys_power)
w1= GetCoefficient(state_group, cpu_power)
w2= GetCoefficient(state_group, mem_power)

sys_fit = GetMatching(state_group, sys_power)
cpu_fit = GetMatching(state_group, cpu_power)
mem_fit = GetMatching(state_group, mem_power)

print('SYS:', [round(i,2) for i in w])
print('CPU:', [round(i,2) for i in w1])

print('MEM:', [round(i,2) for i in w2])
print('CPU PART:', [round(p/q,2) for p,q in zip(w1, w)])
print('MEM PART:', [round(p/q,2) for p,q in zip(w2, w)])
pi = initialEnd

dt2 = 10
recSpeed =  [10]*state_num

wHistory =  []
statHistory=[]
cpu_History=[]
mem_History=[]
sys_History=[]
cpu_predict=[]
mem_predict=[]
sys_predict=[]

cpuConstDeviation = 0
memConstDeviation = 0

cpu_partition=[0.57, 1.0, 0.42, -1.02, 0.5, -1.18, 2.08]
mem_partition=[0.34, -0.0, 0.58, 2.02, 0.5, 2.18, -1.08]
#mem_partition=[0.7, 1, 0.4, -1, 0.5, -1, 2]

while pi < statslen-dt2:
    stepData = [[gp[i] for gp in state_group] for i in range(pi, pi+dt2)]
    power = [sys_power[i] for i in range(pi, pi+dt2)]
    #w = StepRecursion(w, stepData, power, recSpeed)
    
    #print(w)
    #if pi > initialEnd:
    for npi in range(pi, pi+dt2):
        statHistory.append(stepData[npi-pi])
        sys_History.append(sys_power[npi])
        cpu_History.append(cpu_power[npi])
        mem_History.append(mem_power[npi])
    if pi < initialEnd:
        print(w)
        cpuConstDeviation = 0
        for npi in range(pi, pi+dt2):
            cpu_predicti = sum([p*q*r for p,q,r in zip([1]+stepData[npi-pi],w,[0]+cpu_partition)])
            mem_predicti = sum([p*q*r for p,q,r in zip([1]+stepData[npi-pi],w,[0]+mem_partition)])
            cpu_const = w[0] * cpu_predicti/(cpu_predicti+mem_predicti)
            mem_const = w[0] * mem_predicti/(cpu_predicti+mem_predicti)
            cpuConstDeviation += cpu_power[npi]-(cpu_const+cpu_predicti)
            memConstDeviation += mem_power[npi]-(mem_const+mem_predicti)
        cpuConstDeviation = cpuConstDeviation / dt2
        memConstDeviation = memConstDeviation / dt2
    
    #if pi > initialEnd:
    for npi in range(pi, pi+dt2):
        wHistory.append(w)
        sys_predicti=sum([p*q for p,q in zip([1]+stepData[npi-pi],w)])
        sys_predict.append(sys_predicti)
        cpu_predicti = sum([p*q*r for p,q,r in zip([1]+stepData[npi-pi],w,cpu_partition)])
        mem_predicti = sum([p*q*r for p,q,r in zip([1]+stepData[npi-pi],w,mem_partition)])
        #cpu_const = w[0] * cpu_predicti/(cpu_predicti+mem_predicti)
        #mem_const = w[0] * mem_predicti/(cpu_predicti+mem_predicti)
        cpu_predict.append(cpu_predicti)
        mem_predict.append(mem_predicti)
    pi = pi+dt2

wArray = np.array(wHistory).transpose().tolist()

##########################################################################
# This partition print the basic figures.

from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False

plt.plot(sys_History, label='SYS_REAL')
plt.plot(sys_predict, label='SYS_PRED')
#plt.plot(sys_fit, label='SYS_FIT')
plt.title(programName[selectProgram]+' Nodal power and fit power')
plt.ylim((0,400))
plt.xlabel('Time/s')
plt.ylabel('Power/W')
plt.legend()
plt.savefig(programName[selectProgram]+'_Syspower.png')
plt.show()


plt.plot(cpu_History, label='CPU_REAL')
plt.plot(cpu_predict, label='CPU_PRED')
#plt.plot(cpu_fit, label='CPU_FIT')
plt.title(programName[selectProgram]+' CPU real and predicted power')
plt.ylim((0,300))
plt.xlabel('Time/s')
plt.ylabel('Power/W')
plt.legend()
plt.savefig(programName[selectProgram]+'_CPUpower.png')
plt.show()

plt.plot(mem_History, label='MEM_REAL')
plt.plot(mem_predict, label='MEM_PRED')
#plt.plot(mem_fit, label='MEM_FIT')
plt.title(programName[selectProgram]+' MEM real and predicted power')
plt.ylim((0,200))
plt.xlabel('Time/s')
plt.ylabel('Power/W')
plt.legend()
plt.savefig(programName[selectProgram]+'_MEMpower.png')
plt.show()

plt.plot([abs(p-q)/q for p,q in zip(sys_predict, sys_History)], '.', label='SYS_ERROR')
plt.plot([abs(p-q)/q for p,q in zip(cpu_predict, cpu_History)], '.', label='CPU_ERROR')
plt.plot([abs(p-q)/q for p,q in zip(mem_predict, mem_History)], '.', label='MEM_ERROR')
plt.title(programName[selectProgram]+' Deviations')
plt.ylim((0,0.5))
plt.xlabel('Time/s')
plt.ylabel('Relative Error')
plt.legend()
plt.savefig(programName[selectProgram]+'_Error.png')
plt.show()

print('======================= 平均误差 ================================')
print('SYS: '+str(average([abs(p-q)/q for p,q in zip(sys_predict, sys_History)])))
print('CPU: '+str(average([abs(p-q)/q for p,q in zip(cpu_predict, cpu_History)])))
print('MEM: '+str(average([abs(p-q)/q for p,q in zip(mem_predict, mem_History)])))

