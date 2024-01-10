---
title : 'Attention is all you need'
summary : 'Summary of this thesis'
tags : [""]
author : ["Mick"]
draft : true
---

## Recurrent Neural Network
Seq2Seq

Cons: 
1. 阻碍并行化
2. 对长距离有依赖



## Encoder
1. Embedding
	1. word embedding 
	2. positional encoding
4. N times(usually 6)
	1. Multi-head attention: n * d
	2. add-norm(skip-connection and softmax)
	3. feed-forward
	4. add-norm 

## Decoder
![[Pasted image 20230510232321.png]]
1. Embedding 
	1. word embedding 
	2. positional encoding 
2. N times(usually 6)
	1. Masked-multi layer self-attention
		![[Pasted image 20230510231445.png]]
		将没有翻译过的单词(>= i) mask 起来
	1. add-norm
	2. non-self attention: 输入为 Encoder 的直接输出
		 好处：每一位单词都可以利用到 Encoder 所有单词的信息 (这些信息无需 **Mask**)
	1. add-norm 
	2. feed feed-forward 
	3. add-norm 
3. linear
4. softmax 

## Query, Key, Value


## Attention
define:
* n: word counts in the input
* d: dimension of the word embedding(usually 512 = 64 * 8)
* k-dim: col num of Q, K
* v-dim: col num of V

v-dim concated N times should be equals to d, N * v = d

Q: n * dk
K: n * dk
V: n * dv

$Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k} } )V$

1. Attention Score: n * n, a(i, j) 为 i, j 的相关度，且经过归一化(行和为0)
	1. input: n * d matrix of embedding 
	3. Q * K(t) = M1(n * n)
	4. divide by sqrt(64) = 8, **是为了使得在softmax的过程中，梯度下降得更加稳定，避免因为梯度过小而造成模型参数更新的停滞**
	5. softmax normalization 
2. Final attention: n * dv，



## Self Attention
如果 Q 从输入得到，则为self

## Transformer 
1. encoder 
2. decoder 
3. linear(全连接):将解码器产生的向量投影到一个更高维度的词汇表向量（logits）上
4. soft-max
	![[Pasted image 20230510233900.png]]