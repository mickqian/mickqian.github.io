

---
title : ''
summary : 'Summary of this thesis'
tags : [""]
author : ["Mick"]
draft : true
---


## Attention 

Q: T, d_attn
K: T, d_attn 
V: T, d_attn
ab cb => ac 
ac * cb  => ab

Q, K, V 都是 d_attn 隐空间的特征表示

关注度，感兴趣程度，匹配程度

QKt 可以理解为，求两个（自注意力时为一个） latent space 的两个 特征 的相对关注程度(T, T)
得到（相对）注意力后，与 V 相乘，得到加入 K 对 Q 的关注内容的 新特征表示 

Question： 类似于code book？

其后往往接一个全连接层，投影回原来的 d_model 空间


总的来说，
* Cross-Attention 可以加入 k 对 q 中内部结构的感兴趣内容（是人话吗）
* 自注意力可以使输出的特征更关注其自身结构，更自洽

总的来说，Attention 向 q 中 加入了 k 的要求（或者是 k 的信息）
