# ABC
 Artificial Bee Colony Algorithm

人工蜂群算法

## Introduction

人工蜂群算法主要存储在 `ABC.py`中，函数名称为`ABC`，使用时首先`import ABC` ，然后传入相应的参数即可。

`ABC.ABC()`需要的参数依次如下：

> pop: 种群数量
>
> dim: 每个个体的维度
>
> lb: 每个维度的变量下边界,维度为dim
>
> ub: 每个维度的变量上边界,维度为dim
>
> maxIter: 最大迭代次数
>
> fun: 适应度函数

`ABC.ABC()`的返回值共有3个，依次如下：

> GbestScore: 最优适应度值
>
> GbestPosition: 最优解
>
> Curve: 迭代曲线值

项目中给出了示例`Example.py`，详细可以查看求解示例

## Author Info

Author: Xintao Peach

Email: gongzuo.wxt@gmail.com

Page: [XintaoPeach/ABC: Artificial Bee Colony Algorithm (github.com)](https://github.com/XintaoPeach/ABC)
