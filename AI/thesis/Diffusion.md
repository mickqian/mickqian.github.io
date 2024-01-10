forward: 
reverse: 利用 guidance(文本等)，去除噪声

guidance:
	* image classifier
	* image->txt model

ddpm：
* 预测目标 变成 预测噪声(的正态分布)
* 不需要预测方差，只需要均值
improved ddpm:
* 学习方差
* 添加噪声的schedule : 线性 -> 余弦
* 增加模型尺寸
Diffusion model beats GAN:
* 继续加尺寸，attention 加大加宽，single-scale attention -> multi-scale attention
* adaptive group normalization: 以步数为依据的归一化 
* classifier guidance: 图片更逼真，步数更少


Classifier Guided Diffusion:
同时训练 Classifier，用于图像分类
反向过程中，把 Xt 扔给 Classifier，输出一个交叉熵，得到 Gradient（暗含图像生成的目标：有没有含有某个物体）， 帮助采样

利用了额外的模型，训练成本高且不可控

Classifier-Free guidance:
训练时，基于有无监督信号生成两个输出，得到输出之间的相似度，反向过程的时候 进行 apply


diffusion 和 vae 的区别：
* 编码器目标不同：噪声 vs 特征
* bottleneck 尺寸较大
* 多步生成

