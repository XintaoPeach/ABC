"""
人工蜂群算法 Artificial Bee Colony Algorithm
*************************************Chinese******************************************
作者: Xintao Peach
邮箱: gongzuo.wxt@gmail.com
项目地址: 
*************************************English******************************************
Author: Xintao Peach
Email: gongzuo.wxt@gmail.com
Project Address:
"""
import numpy as np
import copy as copy


def initialization(pop,ub,lb,dim):
    '''种群初始化函数'''
    '''
    pop:种群数量
    dim:每个个体的维度
    ub:每个维度的变量上边界,维度为dim
    lb:每个维度的变量下边界,维度为dim
    X:输出的种群,维度为pop*dim
    '''
    X = np.zeros([pop,dim]) # 声明空间，用于存储种群
    for i in range(pop):
        for j in range(dim):
            X[i,j] = (ub[j]-lb[j]) * np.random.random() + lb[j]   # 生成区间[lb,ub]内的随机数
    
    return X


def BorderCheck(X,ub,lb,pop,dim):
    '''边界检查函数'''
    '''
    dim:每个个体的维度
    X:输入的种群,维度为pop*dim
    ub:个体的变量上边界,维度为dim
    lb:个体的变量下边界,维度为dim
    pop:种群数量
    '''
    for i in range(pop):
        for j in range(dim):
            if X[i,j] > ub[j]:
                X[i,j] = ub[j]
            if X[i,j] < lb[j]:
                X[i,j] = lb[j]
    return X


def CaculateFitness(X,fun):
    '''计算适应度函数'''
    pop = X.shape[0] # 种群数量
    fitness = np.zeros([pop,1]) # 声明空间，用于存储种群的适应度值
    for i in range(pop):
        fitness[i] = fun(X[i,:]) # 计算每个个体的适应度值
    return fitness


def SortFitness(Fit):
    '''适应度值的排序'''
    '''
    Fit:输入的种群适应度值,维度为pop*1
    fitness index:输出的适应度值排序后的索引值
    '''
    fitness = np.sort(Fit,axis=0) # 对适应度值进行排序
    index = np.argsort(Fit,axis=0) # 对适应度值进行排序后的索引值
    return fitness,index


def SortPosition(X,index):
    '''个体的排序'''
    '''
    X:输入的种群,维度为pop*dim
    index:输入的适应度值排序后的索引值
    X:输出的种群,维度为pop*dim
    '''
    Xnew = np.zeros(X.shape) # 声明空间，用于存储个体
    for i in range(X.shape[0]):
        # Xnew[i,:] = copy.deepcopy(X[index[i],:]) # 对个体进行排序
        Xnew[i,:] = X[index[i],:]
    return Xnew


def RouletteWheelSelection(P):
    '''轮盘赌选择函数'''
    '''
    Fit:输入的种群适应度值,维度为pop*1
    pop:种群数量
    index:输出的选择后的索引值
    '''
    C = np.cumsum(P) # 计算累计概率
    r = np.random.random() * C[-1] # 定义选择阈值,将随机概率与输入向量P的总和的乘积作为选择阈值
    out = 0  # 初始化索引值
    for i in range(P.shape[0]):
        if r < C[i]:
            out = i
            break
    return out


def ABC(pop,dim,lb,ub,maxIter,fun):
    '''人工蜂群算法'''
    '''
    pop:种群数量
    dim:每个个体的维度
    lb:每个维度的变量下边界,维度为dim
    ub:每个维度的变量上边界,维度为dim
    maxIter:最大迭代次数
    fun:适应度函数
    GbestScore:最优适应度值
    GbestPosition:最优解
    Curve:迭代曲线
    '''
    L = round(0.6 * pop * dim) # 采蜜蜂数量,limit 参数
    C = np.zeros([pop,1]) # 声明空间，用于存储个体的采蜜蜂数量
    nOnlooker = pop  # 引领蜂数量

    X = initialization(pop,ub,lb,dim) # 种群初始化
    fitness = CaculateFitness(X,fun) # 计算适应度值
    fitness,sortIndex = SortFitness(fitness) # 对适应度值进行排序
    X = SortPosition(X,sortIndex) # 对种群进行排序
    GbestScore = copy.copy(fitness[0]) # 记录最优适应度值
    GbestPosition = np.zeros([1,dim]) # 记录最优解
    GbestPosition[0,:] = copy.copy(X[0,:]) # 记录最优解
    Curve = np.zeros([maxIter,1]) # 用于存储迭代曲线
    Xnew = np.zeros([pop,dim]) # 用于存储新的种群
    fitnessNew = copy.copy(fitness) # 用于存储新的适应度值

    for t in range(maxIter):
        # 引领蜂阶段
        for i in range(pop):
            k = np.random.randint(pop)  # 随机选择一个个体
            while k == i:
                k = np.random.randint(pop)
            phi = (2*np.random.random([1,dim])-1)
            Xnew[i,:] = X[i,:] + phi * (X[i,:] - X[k,:])
        Xnew = BorderCheck(Xnew,ub,lb,pop,dim)  # 边界检查
        fitnessNew = CaculateFitness(Xnew,fun)  # 计算适应度值
        for i in range(pop):
            if fitnessNew[i] < fitness[i]:
                X[i,:] = copy.copy(Xnew[i,:])
                fitness[i] = copy.copy(fitnessNew[i])
            else:
                C[i] = C[i] + 1  # 计数器加1
        
        # 计算适应度值
        F = np.zeros([pop,1])
        MeanCost = np.mean(fitness)
        for i in range(pop):
            F[i] = np.exp(-fitness[i] / MeanCost)
        P = F / np.sum(F)

        # 侦察蜂阶段
        for m in range(nOnlooker):
            i = RouletteWheelSelection(P)  # 轮盘赌选择
            k = np.random.randint(pop)  # 随机选择一个个体
            while k == i:
                k = np.random.randint(pop)
            phi = (2*np.random.random([1,dim])-1)
            Xnew[i,:] = X[i,:] + phi * (X[i,:] - X[k,:])  # 侦察蜂搜索,生成新的解,位置更新
        Xnew = BorderCheck(Xnew,ub,lb,pop,dim)
        fitnessNew = CaculateFitness(Xnew,fun)
        for i in range(pop):
            if fitnessNew[i] < fitness[i]:
                X[i,:] = copy.copy(Xnew[i,:])
                fitness[i] = copy.copy(fitnessNew[i])
            else:
                C[i] = C[i] + 1  # 计数器加1
        
        # 判断limit条件,并进行更新
        for i in range(pop):
            if C[i] > L:
                for j in range(dim):
                    X[i,j] = np.random.random() * (ub[j] - lb[j]) + lb[j]
                    C[i] = 0
        fitness = CaculateFitness(X,fun)
        fitness,sortIndex = SortFitness(fitness)
        X = SortPosition(X,sortIndex)
        if fitness[0] < GbestScore:
            GbestScore = copy.copy(fitness[0])
            GbestPosition[0,:] = copy.copy(X[0,:])
        Curve[t] = GbestScore

    return GbestScore,GbestPosition,Curve
