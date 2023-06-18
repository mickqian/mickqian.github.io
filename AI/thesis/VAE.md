
AE:
X-> Encoder -> Feature(Bottleneck) -> Decoder -> X'

DAE: 
corrupt X，降低图片的冗余度（图片的冗余性一般都很高）

以上模型的 Feature 都来自于 图片的编码，而不是源于 Sampling。有了生成随机 Feature Feature的手段（ Sample） 就可以重建图像

VAE:
X -> Encoder -> predict Gaussian Distribution  -> sample a feature from distribution -> Decoder -> X'

VAE 的 distribution 学习难度大，图像尺寸局限（不好做大）

VQVAE:
引入 CodeBook(聚类中心)，把特征转换成更稳定的特征（但同时失去了随机采样的随机性）
X -> Encoder -> Feature -> CodeBook -> Quantized Feature -> Decoder -> X'

pixel CNN

VQVAE2:
* 层级式
* 引入 attention, 根据 codebook 学习 prior: Pixel CNN



## Dall E 2

两阶段：
1. clip 构造对比学习的正负样本对
2. 文本 -> clip encoder -> text embedding -> (diffusion) prior -> image embedding -> diffusion model decoder -> image

diffusion: transformer encoder


transformer encoder 本质上是自回归模型，可以基于自注意力和输入，自回归地生成同类型的内容

![[Pasted image 20230618153050.png]]


![[Pasted image 20230618154911.png]]