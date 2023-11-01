import numpy as np
from matplotlib import pyplot as plt
import ABC

'''适应度函数'''
def fun(X):
    O = X[0]**2 + X[1]**2
    return O


'''利用人工蜂群算法求解x1^2 + x2^2的最小值'''
'''主函数'''
def main():
    # 参数设置
    pop = 50  # 种群数量
    maxIter = 100  # 最大迭代次数
    dim = 2  # 搜索维度
    lb = -10 * np.ones(dim)  # 每个维度的变量下边界
    ub = 10 * np.ones(dim)  # 每个维度的变量上边界
    # 适应度函数的选择
    fobj = fun
    GbestScore,GbestPosition,Curve = ABC.ABC(pop,dim,lb,ub,maxIter,fobj)
    print("最优解的适应度值为: ",GbestScore)
    print("最优解[x1,x2]: ",GbestPosition)

    # 绘制迭代曲线
    plt.figure(2)  # 创建图表1
    plt.plot(Curve,'r-',linewidth=2)  # 画出迭代曲线
    plt.xlabel("Iteration", fontsize='medium')  # x轴标签
    plt.ylabel("Fitness", fontsize='medium')  # y轴标签
    plt.grid(True)  # 显示网格
    plt.title("abcnew", fontsize='large')  # 图表标题
    plt.show()  # 显示图表

if __name__ == '__main__':
    main()
