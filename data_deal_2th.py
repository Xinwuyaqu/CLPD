import time
import os
import re

def timestamp_to_format(timestamp=None, format='%Y-%m-%d %H:%M:%S'):
    if timestamp:
        time_tuple = time.localtime(timestamp)
        res = time.strftime(format, time_tuple)
    else:
        res = time.strftime(format)
    return res


def time_to_timestamp(t):
    timeArray = time.strptime(t, '%Y-%m-%d %H:%M:%S')
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def dstat_time_stamp(itme, format='%Y-%d-%m %H:%M:%S'):
    rtime = '2019-'+itme
    timeArray = time.strptime(rtime, format)
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

datastamp = '2019-12-25-18-45-41-'

def energy_line_to_group(line):
    terms = line.split()
    #print(terms)
    if len(terms) != 11: return (0,0,0,0)
    t = time_to_timestamp(terms[0]+' '+terms[1])
    node = terms[4]
    cpupower = float(terms[7])
    mempower = float(terms[8])
    return (t,node,cpupower,mempower)

def combine_energy(cpu1, cpu2):
    if cpu1[0] == cpu2[0] and cpu1[1] != cpu2[1]:
        return (cpu1[0], cpu1[2]+cpu2[2], cpu1[3]+cpu2[3])
    return (0,0,0)

directories = os.walk('./')
for directory in directories:
    #print(directory)
    if directory[0] == './': continue
    if not directory[0][2:].isdigit(): continue
    energyfile = directory[0] + '/' + datastamp + 'energy'
    dstatfile = directory[0] + '/' + datastamp + 'dstat'
    perffile = directory[0] + '/' + datastamp + 'perf'
    # This partition used to trans the energy data into groups.
    energy = open(energyfile, 'r')
    energylines = energy.readlines()[1:]
    energygroup = [energy_line_to_group(line) for line in energylines]
    resultgroup = []
    while len(energygroup) > 1:
        if energygroup[0][0] == 0:
            energygroup = energygroup[1:]
            continue
        result = combine_energy(energygroup[0], energygroup[1])
        if result[0] == 0:
            energygroup = energygroup[1:]
            continue
        energygroup = energygroup[2:]
        if len(resultgroup) <= 0:
            resultgroup.append(result)
            continue
        if resultgroup[-1][0] >= result[0]: continue
        for it in range(resultgroup[-1][0]+1, result[0]+1):
            resultgroup.append((it, result[1], result[2]))
    #for gp in resultgroup:
    #    print(gp)
    energy.close()
    # This partition used to trans the perf data into groups.
    perf = open(perffile, 'r')
    perflines = perf.readlines()
    
    perf_state_num = 0
    perf_state_name = []
    perfresult = []
    currentcol = 0
    perf_time_basic = int(perflines[0])
    last_time_stamp = 0
    for line in perflines[2:]:
        terms = line.split()
        time_stamp = float(terms[0])
        if last_time_stamp == 0 or last_time_stamp == time_stamp:
            perf_state_num += 1
            perf_state_name.append(terms[2]+',')
            last_time_stamp = time_stamp
        else: break

    print('perf_state_num:',perf_state_num)
    print('perf_state_name:',perf_state_name)
    
    for line in perflines[2:]:
        terms = line.split()
        if '#' in terms[0]: continue
        currentcol += 1
        if currentcol > perf_state_num:
            currentcol = 1
        if currentcol == 1:
            #print(terms[0])
            perfresult.append([perf_time_basic+int(float(terms[0]))]+['']*perf_state_num)
        if len(perfresult) > 0:
            perfresult[-1][currentcol] = terms[1].replace(',','')
    print(len(perfresult))
    print(perfresult[0])
    perfgroup = []
    for group in perfresult:
        if len(perfgroup) <= 0:
            perfgroup.append(group)
            continue
        if group[0] <= perfgroup[-1][0]: continue
        for it in range(perfgroup[-1][0]+1, group[0]+1):
            perfgroup.append([it]+group[1:])
    print(len(perfgroup))
    print(perfgroup[0])
    perf.close()
    #for group in perfgroup:
    #    print(group)
    # This partition used to trans the dstat data into groups.
    dstat = open(dstatfile, 'r')
    dstatlines = dstat.readlines()[5:]
    dstatresult = []
    for line in dstatlines[1:]:
        terms = re.split('"|,|\n|\r', line.strip())
        #print(terms)
        t = dstat_time_stamp(terms[-3])
        if len(dstatresult) <= 0:
            dstatresult.append((t,line))
            continue
        if dstatresult[-1][0] >= t: continue
        for it in range(dstatresult[-1][0]+1, t+1):
            dstatresult.append((it,line.strip()))
    #for group in dstatresult:
    #    print(group)
    dstat.close()
    # This partition used to combined all the data from the three groups.
    # dstatresult, perfgroup, resultgroup
    combineresult = []
    while len(dstatresult) > 0 and len(perfgroup) > 0 and len(resultgroup) > 0:
        if(max(dstatresult[0][0],perfgroup[0][0],resultgroup[0][0])==min(dstatresult[0][0],perfgroup[0][0],resultgroup[0][0])):
            combineresult.append((resultgroup[0],perfgroup[0],dstatresult[0]))
            dstatresult=dstatresult[1:]
            perfgroup=perfgroup[1:]
            resultgroup=resultgroup[1:]
            continue
        if(min(dstatresult[0][0],perfgroup[0][0],resultgroup[0][0]) == dstatresult[0][0]):
            dstatresult=dstatresult[1:]
            continue
        if(min(dstatresult[0][0],perfgroup[0][0],resultgroup[0][0]) == perfgroup[0][0]):
            perfgroup=perfgroup[1:]
            continue
        if(min(dstatresult[0][0],perfgroup[0][0],resultgroup[0][0]) == resultgroup[0][0]):
            resultgroup=resultgroup[1:]
            continue
    
    outputcsv = directory[0] + '/' + datastamp + '-result.csv'
    output = open(outputcsv, 'w')
    output.write('time,CPU_POWER,MEM_POWER,time,'+''.join(perf_state_name)+'time,'+dstatlines[0])
    #output.write('time,CPU_POWER,MEM_POWER,time,LLC-loads,LLC-load-misses,LLC-stores,LLC-store-misses,cache-misses,time,'+dstatlines[0])
    
    for group in combineresult:
        line = timestamp_to_format(group[0][0])
        line += ','+str(group[0][1])+','+str(group[0][2])+','
        
        line += timestamp_to_format(group[1][0])+','
        for data in group[1][1:]:
            line += str(data)+','
        line += timestamp_to_format(group[2][0])+','
        line += group[2][1]+'\n'
        output.write(line)
    output.close()
    

# -*- coding: utf-8 -*-
 
#导入需要使用的包
import xlrd  #读取Excel文件的包
import xlsxwriter   #将文件写入Excel的包
 
import csv
import xlwt

'''
#函数入口
#定义要合并的excel文件列表
directories = os.walk('./')
for directory in directories:
    if directory[0] == './': continue
    if not directory[0][2:].isdigit(): continue
    csvfile = directory[0] + '/' + datastamp + '-result.csv'
    wb=xlsxwriter.Workbook(directory[0]+'/result.xlsx')
    ws=wb.add_worksheet(directory[0][2:])
    f = open(csvfile, 'r')
    read = csv.reader(f)
    l = 0
    for line in read:
        r = 0
        for i in line:
            value = i
            if '.' in i:
                value = float(i)
            elif i.isdigit():
                value = int(i)
            ws.write(l, r, value)  # 一个一个将单元格数据写入
            r = r + 1
        l = l + 1
    wb.close()
    '''


#函数入口
#定义要合并的excel文件列表
directories = os.walk('./')
wb=xlsxwriter.Workbook('result.xlsx')
for directory in directories:
    if directory[0] == './': continue
    if not directory[0][2:].isdigit(): continue
    csvfile = directory[0] + '/' + datastamp + '-result.csv'
    ws=wb.add_worksheet(directory[0][2:])
    f = open(csvfile, 'r')
    read = csv.reader(f)
    l = 0
    for line in read:
        r = 0
        for i in line:
            value = i
            if '.' in i:
                value = float(i)
            elif i.isdigit():
                value = int(i)
            ws.write(l, r, value)  # 一个一个将单元格数据写入
            r = r + 1
        l = l + 1
wb.close()










