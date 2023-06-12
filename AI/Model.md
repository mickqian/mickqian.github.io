## 速记
mlp: Flatten + FAF



# CLIP
训练： text encoder, image encoder, contrastive loss, joint multimodal embedding
推理： labels + template -> text encoder, similarity with encoded image

# Dall-E


# LeNet
# AlexNet 2012
![[Pasted image 20230609205327.png]]
类似于 LeNet:
* AlexNet: 8 层， C(M)C(M)CCC(M)FFF, 五个卷积层、两个全连接隐藏层和一个全连接输出层，使用 ReLU
* LeNet: 5层， C(M)C(M)FFF, 两个卷积层两个全连接隐藏层和一个全连接输出层，Sigmoid
# ResNet
![[Pasted image 20230609205940.png]]
# DenseNet
输出是 *连接*， 而不是 *相加*，因此每一时刻的输出都与此前所有层的输出相联系
使用过渡层： 1 * 1 , stride = 2 的卷积层 减少通道数，控制模型复杂度

# GRU
非循环神经网络，由于矩阵的连续乘积，可以导致 *梯度消失* 等问题
* reset gate: 控制过去状态的数量
* update gate: 控制新状态中的旧状态副本数量 ，剩余为新隐状态

$$
\begin{align}
R_{t} = \sigma(X_{t}W_{xr} + H_{t-1}W_{hr} + b_{r})
\\
Z_{t} = \sigma(X_{t}W_{xz} + H_{t-1}W_{hz} + b_{z})
\\


\tilde H_{t} =tanh(X_{t}W_{xh} + (R_{t} \odot H_{t-1})W_{hh} + b_h)

\\

H_{t} = Z_{t} \odot H_{t - 1} + (1 - Z_{t}) \odot \tilde H_{t}
\end{align}
$$

# LSTM 1997
memory cell/cell: similar to latent state, 记录附加的信息
* output gate: 
* input gate: 采用多少来自 $\tilde C_{t}$ 的新数据
* forget gate: 重置单元内容
* candidate memory cell
	* $$ \tilde C_t = tanh(X_tW_{xc} + H_{t-1}W_{hc} + b_c) $$

与 GRU 类似，能够通过专用机制决定什么时候记忆或忽略**隐状态中的输入**
![[Pasted image 20230609220125.png]]


# Multimodal

# CNN
强大的 inductive bias

## VIT Vision Transformer 2020
transformer 视觉，数据足够多时，突破 *transformer 缺少 Inductive Bias(一种先验知识）* 的限制，超过 CNN

推理：
224 * 224 * 3 => 14 * 14  = 196 个 , 16 * 16 * 3 = 768 的 patch => patch 投影 + postion embedding + extra \[class=cls\] embedding => encoder =>  cls 对应的输出 $z^{0}_{L}$ 作为最终输出的类别预测(logits)