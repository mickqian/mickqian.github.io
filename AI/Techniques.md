


## Regularization
正则化，降低模型复杂度，防止 overfitting

tan h: 当 |x| 比较小 时，接近线性网络

复杂度的衡量： 
	* 参数数量
	* 参数绝对值

手段：
* 向损失函数中引入正则项，将模型参数的范数作为惩罚
* Dropout: 训练时，随机屏蔽（置0）并对结果进行 scale
	* 原理：Don't rely on any one feature(neuron), spread out weights
	* 随机淘汰网络中的一些单元，因此训练时，每层不会对任意一个神经元施加 **太多权重**，这种分散权重的方式防止了过拟合
	*  迫使同层节点对输出承担或多或少的责任，增强模型的泛化性，因为它不会太依赖某些局部的特征
* Data augmentation
	* 增加数据集的泛化性
* Early stopping 
	* 在权重overfit之前结束，但 error 较高
* 


## Normalize
对于随机输入数据，会导致**成本函数**对每个维度的scale 不一致(elongated)，导致参数调整出现很多 oscillate

* z-score
* min-max
	![[Pasted image 20230510221729.png]]
* softmax: normalized exponential function  

### Batch Norm
对**每一批**训练数据进行归一化， 

effect: 
* **reduce shift** on train data
* 增加模型的鲁棒性，提升训练速度 

在 z/a 上作用

why work?
* learning on shifting input distribution: 偏移在神经网络中会产生累积，导致后面的层的输入不稳定


### Layer Norm


不是全量数据集，因为容易过拟合



## Bias
Inductive bias
