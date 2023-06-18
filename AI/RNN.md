目标:
* 自回归模型：对自己执行回归 
	* $P(x_t|x_{t-1},...,x_1)$
* Latent autoregressive models
	* 引入 latent variable $h_t$：作为总结

```python
for X, y in train_iter:  
	// X: 输入, y: 标签
	trainer.zero_grad()  
	// 将net输出与y求loss
	l = loss(net(X), y) 
	// 对loss进行反向传播 
	l.sum().backward()  
	trainer.step()
```

k-step ahead prediction: 错误的累积


## NLP
vocab: token 的映射
corpus:  token 的频率  map

频率最高的词: stop words，可以被过滤
词频衰减很快
拉普夫定律
拉普拉斯



## Optimizer
adam: sgd优化器



## 循环神经网络

交叉熵：信息论
perplexity:  一个序列中 n 个词元的**交叉熵损失**的平均值，用于评价 LM 的性能

梯度裁剪:
梯度爆炸：
梯度消失：

animator：





