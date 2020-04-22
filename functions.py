
import xlrd
import xlwt
import math
import numpy  as np
import pandas as pd
from numpy import mat

################## function average ############################

def average(l):
    if len(l) == 0: return 0
    return sum(l)/len(l)

################## function SingleList #########################

def SingleList(l):
    result = []
    for sl in l:
        result = result + sl
    return result

################## function GetLocalMax ########################

def GetLocalMax(l, size=20):
    if len(l) <= 0: return 0
    if len(l) <= size: return max(l)
    m = []
    for i in range(size, len(l)):
        m.append(max(l[i-size:i]))
    return sum(m)/len(m)

################## function GetLocalMin ########################

def GetLocalMin(l, size=20):
    if len(l) <= 0: return 0
    if len(l) <= size: return min(l)
    m = []
    for i in range(size, len(l)):
        m.append(min(l[i-size:i]))
    return sum(m)/len(m)

################## function Normalize ##########################

def Normalize(l, amin=0, amax=1):
    mx = max(l)
    mn = min(l)
    if mx == mn and mx != 0:
        return [amax] * len(l)
    if mx > mn:
        return [(k-mn) / (mx - mn) * (amax-amin) + amin for k in l]
    return [amin]*len(l)
################### function Filter ############################

def Filter(l, size=10):
    result = []
    for i in range(0, len(l)):
        if i < size:
            result.append(sum(l[0:i+1]) / (i+1))
        else:
            result.append(sum(l[i-size+1:i+1]) / size)
    return result
################## function GetWaveSize ########################

def GetWaveSize(l, size=10):
    result = []
    for i in range(0, len(l)):
        if i < size:
            result.append(max(l[0:i+1])-min(l[0:i+1]))
        else:
            result.append(max(l[i-size+1:i+1])-min(l[i-size+1:i+1]))
    return result

################## function GetCoefficient #####################

# 计算系数：
# 输入：状态值，观测值
# 输出：状态值系数及常数项
def GetCoefficient(stats, obsv):
    jstatNum = len(stats)                                           # 状态值数量
    statsNum = [len(stati) for stati in stats] + [len(obsv)]       # 各状态值数量
    minus = min(statsNum)                                          # 取最小值（防止各状态值数量不同无法构成正确的矩阵）
    nstat = [[1]*minus] + [stati[:minus] for stati in stats]      #
    nobsv = obsv[:minus]                                           #
    statArray = mat(nstat).transpose()                             # 构造矩阵X
    obsvArray = mat(nobsv).transpose()                             # 构造矩阵Y
    statTrans = mat(nstat)                                         # 构造矩阵XT
    
    # 计算结果
    statSqure = statTrans*statArray
    if np.linalg.det(statSqure) == 0:
        print('输入数据成奇异矩阵')
        return []
    coefficient = np.linalg.inv(statSqure)*statTrans*obsvArray # ((XT*X)-1)*XT*Y
    return coefficient.transpose().tolist()[0]

################## function GetCoefficientNoConst #####################

# 计算系数：
# 输入：状态值，观测值
# 输出：状态值系数
def GetCoefficientNoConst(stats, obsv):
    jstatNum = len(stats)                                           # 状态值数量
    statsNum = [len(stati) for stati in stats] + [len(obsv)]       # 各状态值数量
    minus = min(statsNum)                                          # 取最小值（防止各状态值数量不同无法构成正确的矩阵）
    nstat = [stati[:minus] for stati in stats]                    #
    nobsv = obsv[:minus]                                           #
    statArray = mat(nstat).transpose()                             # 构造矩阵X
    obsvArray = mat(nobsv).transpose()                             # 构造矩阵Y
    statTrans = mat(nstat)                                         # 构造矩阵XT
    
    # 计算结果
    statSqure = statTrans*statArray
    if np.linalg.det(statSqure) == 0:
        print('输入数据成奇异矩阵')
        return []
    coefficient = np.linalg.inv(statSqure)*statTrans*obsvArray # ((XT*X)-1)*XT*Y
    return coefficient.transpose().tolist()[0]

################### function StepRecursion ###############################
# w为待递归系数向量，s为t组状态值矩阵，P为t个观测值，speed为步进速度

def StepRecursion(w, s, P, speed):
    t = len(s)
    if t <= 0: return w
    statnum = len(s[0])+1
    stats = [[1]+sj for sj in s]
    stepj = [0]*statnum
    # print(stats)
    # exit()
    Pe = sum([w[i]*stats[t-1][i] for i in range(0,statnum)])
    #print(Pe)
    for j in range(0,t):
        Pe = sum([w[i]*stats[j][i] for i in range(0,statnum)])
        #print("Predict Power:", j, ", ", Pe)
        Pj = P[j]
        #print(Pe, Pj)
        for i in range(0,statnum):
            stepj[i] = stepj[i] + (Pe - Pj) * stats[j][i]/(Pj*Pj)
            #if Pe > Pj: print('True')
        #print("Coefficients:", j, ", ", stepj)
    #step_size = math.sqrt(sum([p*p for p in stepj]))
    #P_step = sum([p*q for p,q in zip(stepj, stats[t-1])])
    #if Pe != Pj: step_size = P_step * speed[0] * 2 / (Pe - Pj)
    #if step_size != 0: stepj = [p / step_size for p in stepj]
    newW = [w[i]-2*speed[i]*stepj[i] for i in range(0,statnum)]
    Pe = sum([newW[i]*stats[t-1][i] for i in range(0,statnum)])
    #print(Pe)
    return newW
    
################### function StepRecursionNoConst ###############################
# w为待递归系数向量，s为t组状态值矩阵，P为t个观测值，speed为步进速度

def StepRecursionNoConst(w, s, P, speed):
    t = len(s)
    if t <= 0: return w
    statnum = len(s[0])
    stats = s
    omiga = w[1:]
    stepj = [0]*statnum
    # print(stats)
    # exit()
    Pe = sum([w[i]*stats[t-1][i] for i in range(0,statnum)])
    #print(Pe)
    for j in range(0,t):
        Pe = sum([omiga[i]*stats[j][i] for i in range(0,statnum)])
        #print("Predict Power:", j, ", ", Pe)
        Pj = P[j]-w[0]
        #print(Pe, Pj)
        for i in range(0,statnum):
            stepj[i] = stepj[i] + (Pe - Pj) * stats[j][i]/(Pj*Pj)
            #if Pe > Pj: print('True')
        #print("Coefficients:", j, ", ", stepj)
    #step_size = math.sqrt(sum([p*p for p in stepj]))
    #P_step = sum([p*q for p,q in zip(stepj, stats[t-1])])
    #if Pe != Pj: step_size = P_step * speed[0] * 2 / (Pe - Pj)
    #if step_size != 0: stepj = [p / step_size for p in stepj]
    newW = [w[0]] + [omiga[i]-2*speed[i]*stepj[i] for i in range(0,statnum)]
    Pe = sum([newW[i]*stats[t-1][i] for i in range(0,statnum)])
    #print(Pe)
    return newW
################## function Resize #########################################

def Resize(lst, c):
    return [i*c for i in lst]
    

################### function GetMatching #########################

def GetMatching(stats, obsv):
    coefficient = GetCoefficient(stats, obsv)
    return (np.mat([[1]*len(obsv)]+stats).transpose()*(np.mat(coefficient).transpose())).transpose().tolist()[0]
################### function GetMultiplySum ############################

def GetMultiplySum(lst1, lst2):
    return sum(m*n for m,n in zip(lst1, lst2))

################### function GetDeviation ########################

# 计算误差值（绝对值和百分比）
# 输入：状态值，观测值
# 输出：每个观测值的误差
def GetDeviation(stats, obsv):
    coefficient = GetCoefficient(stats, obsv)
    prediction = mat([[1]*len(stats[0])] + stats).transpose() * mat(coefficient).transpose()
    obsvArray = mat(obsv).transpose()
    deviationArray = (prediction - obsvArray).transpose()
    deviation = deviationArray.getA().tolist()
    deviation = [abs(i) for i in deviation[0]]
    deviationRate = [[m,m/abs(n)] for m,n in zip(deviation, obsv)]
    return deviationRate

######################## end function #############################

