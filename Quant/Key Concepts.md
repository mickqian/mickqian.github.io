## 凸优化
找出使凸函数值最小的x，为全局最优值
局部最优解一定是全局最优解

## 方法
* 梯度下降
* 牛顿法
* 拟牛顿法



## 傅立叶变换 Fourier Transformation
* $x[n]$: 信号
* $X[k]$: 频率为 k 的震荡函数的级数（cos, sin）

缺点：
1. 不能刻画时间域上信号的局部特性
2. 对突变和非平稳信号的效果不好，没有时频分析


Gibbs效应：



## FS Fourier Series
$$

\begin{align} f(t)&=\frac{a_{0}}{2}+\sum_{n=1}^{\infty}{[a_{n}cos(n\omega t)+b_{n}sin(n\omega t)]}  \tag{1}  \\

&a_{n}=\frac{2}{T}\int_{t_{0}}^{t_{0}+T}f(t)cos(n\omega t)dt \tag{2} \\ 
 
&b_{n}=\frac{2}{T}\int_{t_{0}}^{t_{0}+T}f(t)sin(n\omega t)dt \tag{3}\\ \end{align}
$$

### DFT
$X[k]=\sum_{n=0}^{N-1}e^{-j\frac{2\pi}{N}{nk}}x[n]$ 

#### IDFT

#### FFT Fast Fourier Transform 快速傅立叶变换
将 DFT 矩阵分解成稀疏因子的乘积来快速计算
是 DFT 算法

$X(K)=\sum_{r=0}^{\frac{N}{2}-1}x(2r)W_{\frac{N}{2}}^{rk}+W_N^r\sum_{r=0}^{\frac{N}{2}-1}x(2r+1)W_{\frac{N}{2}}^{rk}$

[推导过程](https://blog.csdn.net/enjoy_pascal/article/details/81478582)

#### 欧拉公式
$e^{i\theta}=cos\theta+i\cdot sin\theta$


### STFT 短时傅立叶变换
加窗傅立叶变换 -> 局部性
![[Pasted image 20230512231535.png]]
窗太小 -> 频率分辨率差
窗太大 -> 时间分辨率差


海森堡不确定性：我们不能同时获取一个粒子的动量和位置，我们也不能同时获取信号绝对精准的时刻和频率




## 小波变换 Wavelet transform

基的正交性：充分条件
基具有完备性即可
基的表示有唯一性

时频分析

![[Pasted image 20230512231658.png]]

$\tau$: 移量
$a$: 横向尺度，对应频率（反比）
t 时刻，频率为 a 的正弦波的振幅



解决局部性
解决时频分析

#### 多频率分析


#### 父小波 母小波
任何小波变换的基函数，其实就是对母小波和父小波缩放和平移的集合

#### 多分辨率分析

### References:
[小波变换（wavelet transform）的通俗解释](https://www.cnblogs.com/jfdwd/p/9249850.html)

