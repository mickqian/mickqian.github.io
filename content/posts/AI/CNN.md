
---
title : ''
summary : 'Summary of this thesis'
tags : [""]
author : ["Mick"]
draft : true
---


## NiN



## Inception 
concat channels of:
* convs
* pool
![[Pasted image 20230618142549.png]]



## Yolo


## Unet

* Down sampling:
	(conv, relu , max-pool) * 4 times
	increase channels
* Up sampling:
	transpose conv on skip-connect concated features , pool
	shrink channels


## Style Transfer

J = Content loss + Style loss
C, S, G
Content loss: loss between G and C， using pre-trained ConvNet(E.g., VGG)
Style loss: loss between styles of G and S
	* Style 的定义：特征里，不同通道之间的互相关性
	* 

Update G by gradient descent(因为 G 出现在 J 里，因此可用 J 对 G 求导，所以可以进行更新)